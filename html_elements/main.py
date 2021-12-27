import webview
from playsound import playsound

#import jinja2
from jinja2 import Template


# https://techmonger.github.io/69/jinja2-render-html/



class Api():
    def __init__(self, window):
        self.window = window

    def on_color_select(self, c):
        print(c)

    def open_file_chooser(self):
         file_types = ('Image Files (*.bmp;*.jpg;*.gif)', 'All files (*.*)')
         paths = self.window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
         print(paths)

    def on_radio_changed(self, id):
        print(id)     

    def play_a_sound(self):
        playsound("./static/out.mp3")

    def on_drop_down_changed(self, selected):
        print(selected)    



# url alone just loads a static html file
#win = webview.create_window("webtech is great", url="index.html")   
#html=html doesn't link assets

# solution: prepare html from template, save to tmp file, load that as url


html = open("index.html", "r").read()
rendered = Template(html).render(words=["sopra", "la", "panca" ,"la" ,"capra", "campa", "sotto", "la", "panca", "la", "capra", "crepa"])


with open("tmp.html", "w") as f:
    f.write(rendered)


win = webview.create_window("webtech is great", url="tmp.html")  

#win.load_url("index.html")


api = Api(win) 
win._js_api = api


webview.start()