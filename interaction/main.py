import webview

class Api():

    """
    Defines some methods that can be called from js.
    """
    def __init__(self):
        pass

    def test_print(self):
        print("hello world!")

    def print_obj(self, string):
        print(string)


api=Api()

# create a new window, give it html and an Api object
win = webview.create_window("my app", url="index.html", js_api=api)
# start the window. Arguments are to execute a function on start
webview.start(lambda win: print(win.get_elements("#my_field")) , win)
# GUI loop started, no more code...


# get element by id from python
# win.get_elements("#my_field") 

# get element by class from python
# win.get_elements(".my_class") 




