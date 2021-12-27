from pynput import keyboard
import webview


win = webview.create_window("test keys", url="index.html")



def on_press(key):
    v = win.evaluate_js(f" document.getElementById('key_pressed').innerHTML = \"{str(key)}\" ")


listener = keyboard.Listener(on_press = on_press)
listener.start()

webview.start()