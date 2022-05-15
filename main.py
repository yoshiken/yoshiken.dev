from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import markdown
import shutil
import glob


def index_page(env):
    template = env.get_template("index/base.j2")
    with open("docs/index.html", mode='w') as f:
        f.write(template.render())


def about_page(env):
    md = markdown.Markdown()
    with open("content/about.md") as f:
        s = f.read()
        text = md.convert(s)
    template = env.get_template("about/base.j2")
    with open("docs/about.html", mode='w') as f:
        f.write(template.render({'body_text': text}))


def cp_favicon():
    shutil.copyfile("./template/static/favicon.ico", "./docs/favicon.icon")


def articles_page(env):
    output_dir = "docs/articles"
    os.makedirs(output_dir, exist_ok=True)
    md = markdown.Markdown()
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
    env = Environment(
        loader=FileSystemLoader("template"),
        autoescape=select_autoescape()
    )
    index_page(env)
    about_page(env)
    cp_favicon()
    articles_page(env)
