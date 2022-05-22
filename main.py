from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import markdown
import shutil
import glob
import re
from datetime import datetime


def convert_index_page(env, articles):
    template = env.get_template("index/base.j2")
    with open("docs/index.html", mode='w') as f:
        f.write(template.render({'articles': articles}))


def convert_unique_pages(env, md, unique_pages):
    for page in unique_pages:
        with open("content/" + page + ".md") as f:
            s = f.read()
            text = md.convert(s)
        template = env.get_template("about/base.j2")
        with open("docs/" + page + ".html", mode='w') as f:
            f.write(template.render({'body_text': text}))


def cp_favicon():
    shutil.copyfile("./template/static/favicon.ico", "./docs/favicon.icon")


def cp_ogpimg():
    shutil.copyfile("./template/static/ogp.png", "./docs/ogp.png")


def convert_articles(md):
    articles_list = glob.glob("./content/articles/*")
    articles = []
    for article in articles_list:
        tmp_txt = ""
        with open(article) as f:
            body = {}
            lines = f.readlines()
            for line in lines:
                if line.startswith("Title:"):
                    body['title'] = re.sub('^Title: ', "", line).replace('\n', '')
                    continue
                if line.startswith("Date:"):
                    date_str = re.sub('^Date: ', "", line).replace('\n', '')
                    body['date'] = datetime.strptime(date_str + '+09:00', '%Y-%m-%d %H:%M:%S%z')
                    continue
                if line.startswith("Summary:"):
                    body['summary'] = re.sub('^Summary: ', "", line).replace('\n', '')
                    continue
                if line.startswith("Category:"):
                    body['category'] = re.sub('^Category: ', "", line).replace('\n', '')
                    continue
                tmp_txt += line
            body['text'] = md.convert(tmp_txt)
            body['output_file_name'] = os.path.splitext(os.path.basename(article))[0]
            articles.append(body)
    sorted_articles = sorted(articles, key=lambda x: x['date'], reverse=True)
    return sorted_articles


def output_aricles_pages(env, articles):
    output_dir = "docs/articles/"
    os.makedirs(output_dir, exist_ok=True)
    template = env.get_template("articles/base.j2")
    for article in articles:
        with open(output_dir + article['output_file_name'] + ".html", mode='w') as f:
            f.write(template.render({'article': article}))


if __name__ == "__main__":
    os.makedirs("docs", exist_ok=True)
    md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'abbr'])
    env = Environment(
        loader=FileSystemLoader("template"),
        autoescape=select_autoescape()
    )
    unique_pages = ["about", "format"]
    convert_unique_pages(env, md, unique_pages)
    cp_favicon()
    cp_ogpimg()
    articles = convert_articles(md)
    output_aricles_pages(env, articles)
    convert_index_page(env, articles)
