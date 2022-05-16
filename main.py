from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import markdown
import shutil
import glob
import re


def index_page(env):
    template = env.get_template("index/base.j2")
    with open("docs/index.html", mode='w') as f:
        f.write(template.render())


def about_page(env, md):
    with open("content/about.md") as f:
        s = f.read()
        text = md.convert(s)
    template = env.get_template("about/base.j2")
    with open("docs/about.html", mode='w') as f:
        f.write(template.render({'body_text': text}))


def cp_favicon():
    shutil.copyfile("./template/static/favicon.ico", "./docs/favicon.icon")


def convert_articles(env, md):
    articles_list = glob.glob("./content/articles/*")
    articles = []
    for article in articles_list:

        tmp_txt = ""
        with open(article) as f:
            body = {}
            lines = f.readlines()
            for line in lines:
                print("".join(lines))
                if line.startswith("Title:"):
                    body['tile'] = re.sub('^Title:', "", line)
                    continue
                if line.startswith("Date:"):
                    body['date'] = re.sub('^Date:', "", line)
                    continue
                if line.startswith("Summary:"):
                    body['summary'] = re.sub('^Date:', "", line)
                    continue
                if line.startswith("Category:"):
                    body['category'] = re.sub('^Category:', "", line)
                    continue
                tmp_txt.join(line)
            body['text'] = md.convert(tmp_txt)
            body['output_file_name'] = os.path.splitext(os.path.basename(article))[0] + ".html"
            articles.append(body)
    return articles


    output_dir = "docs/articles"
    os.makedirs(output_dir, exist_ok=True)

    articles_list = glob.glob("./content/articles/*")
    for article in articles_list:
        template = env.get_template("articles/base.j2")
        with open(article) as f:
            s = f.read()
            text = md.convert(s)
            output_file_name = os.path.splitext(os.path.basename(article))[0] + ".html"
        with open(output_dir + "/" + output_file_name, mode='w') as f:
            f.write(template.render({'body_text': text}))


if __name__ == "__main__":
    os.makedirs("docs", exist_ok=True)
    md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'abbr'])
    env = Environment(
        loader=FileSystemLoader("template"),
        autoescape=select_autoescape()
    )
    index_page(env)
    about_page(env, md)
    cp_favicon()
    articles_page(env, md)
