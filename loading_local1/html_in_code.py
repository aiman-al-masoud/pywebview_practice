import webview

webview.create_window("hello world", html="""
<style>
p{ color: red}
</style>
<p>HELLO WORLD   </p>""")


webview.start()

