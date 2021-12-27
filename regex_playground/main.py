import webview
import re


class Api:
    def __init__(self):
        pass

    def matches(self, regex, string):
        return bool(re.match(regex, string))



api = Api()
win = webview.create_window("Regex Playground", url="index.html", js_api=api)


webview.start()

