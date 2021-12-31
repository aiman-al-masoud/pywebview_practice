import webview
from jinja2 import Template
from random import randint

"""
Rendering a template via jinja2, saving rendered html to temporary file, 
reloading page from python by passing url of file w/ Window.load_url .

"""


TMP = "tmp.html"

class Api:
    def __init__(self, window):
        self.window = window

    def reload(self):
        i = str(randint(1, 100))
        print(i)

        with open("index.html", "r") as f:
            template = f.read()

        html = Template(template).render(parameter=i)

        with open(TMP, "w+") as f:
            f.write(html)
        self.window.load_url(TMP)

win = webview.create_window("title", url="index.html")

api = Api(win)

win._js_api = api

webview.start()