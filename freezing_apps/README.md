Intsall the pyinstaller module

```
$ pip install pyinstaller
```

Navigate to the directory where your main.py is stored:

```
$ ls
main.py
```

Run this command (It may take a while):

```
pyinstaller main.py --onefile --icon=="icon.ico"
```

You should be able to find and run your single executable file in the dist directory that was just created:

```
$ cd dist
$ ls
main
$ ./main
```

The executable's size may be very large (hundreds of MBs). But it should work without the need of a Python interpreter, provided it is run on a machine with binary compatibility with the machine it was compiled on.

This method was tested and works with Pywebview (tried it on Linux).





