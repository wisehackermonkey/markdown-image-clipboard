#  gui for starting and stopping the websocket client
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210215


from tkinter import *

running = True  # Global flag
idx = 0  # loop index

def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False

root = Tk()
root.title("Markdown Image Clipboard (pushbullet)")
root.geometry("400x100")

app = Frame(root)
app.pack()

start = Button(app, justify="center",text="Start", command=start)
stop = Button(app, justify="center",text="Stop", command=stop)
_quit = Button(root, justify="center", text="Quit", command=root.quit)
_quit.pack()
start.pack()
stop.pack()

while True:
    if idx % 500 == 0:
        root.update()

    if running:
        print("hello")
        idx += 1