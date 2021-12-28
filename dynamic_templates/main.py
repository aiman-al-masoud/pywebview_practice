import webview
from jinja2 import Template


with open("index.html", "r") as f:
    t = f.read()


words=[f'cat number {i}' for i in range(100)]

r = Template(t).render(words=words)

with open("tmp.html", "w") as f:
    f.write(r)

win = webview.create_window("Dynamic Content", url="tmp.html")

webview.start()
