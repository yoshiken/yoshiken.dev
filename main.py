from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import markdown
import shutil


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


if __name__ == "__main__":
    os.makedirs("docs", exist_ok=True)
    env = Environment(
        loader=FileSystemLoader("template"),
        autoescape=select_autoescape()
    )
    index_page(env)
    about_page(env)
    cp_favicon()
