#  gui for starting and stopping the websocket client
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20210215

import os
import json
import time
import requests
import websocket
import pyperclip
from dotenv import load_dotenv

load_dotenv()



PUSHBULLET_API_KEY = os.getenv("PUSHBULLETAPI")
if not PUSHBULLET_API_KEY:
    print("ERROR: please add PUSHBULLETAPI=<API KEY HERE> to your path")
    exit()

# endpoint to check if a user has done anything, if so do a action "on_message(ws, message):"
pushbullet_websocket_api_url = f"wss://stream.pushbullet.com/websocket/{PUSHBULLET_API_KEY}"

# endpoint used to grab the image from the user
pushbullet_pushes_api_url = f"https://api.pushbullet.com/v2/pushes"
# api key is passed as a header for this endpoint
# headers = {"Access-Token": PUSHBULLET_API_KEY}

headers = {"Access-Token": PUSHBULLET_API_KEY,
            "active":"true",
            "limit": "1",
            "modified_after":"0.0"}

last_push_timestap = 0.0# used for getting the most recent push

print(pushbullet_websocket_api_url)



# [python - How do you create a Tkinter GUI stop button to break an infinite loop? - Stack Overflow](https://stackoverflow.com/questions/27050492/how-do-you-create-a-tkinter-gui-stop-button-to-break-an-infinite-loop)
from tkinter import *
from threading import Thread

def scanning():
    websocket.enableTrace(True)
    global ws
    ws = websocket.WebSocketApp(pushbullet_websocket_api_url,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

    

def start_thread():
    # Assign global variable and initialize value
    global stop
    stop = 0

    # Create and launch a thread 
    t = Thread (target = scanning)
    t.start()

def stop():
    # Assign global variable and set value to stop
    global stop
    stop = 1
    ws.close()

root = Tk()
root.title("Markdown-Image-Clipboard")
root.geometry("400x100")

app = Frame(root)
app.grid()

start = Button(app, text="Start Scan",command=start_thread)
stop = Button(app, text="Stop",command=stop)

start.grid()
stop.grid()








try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    json_message = dict(json.loads(message))
    
    print(f"Message: {message}")
    
    if "subtype" in json_message:
        # if json_message["subtype"] == "push":
        print("grabbing pushed data")
        latest_pushes = requests.get(pushbullet_pushes_api_url,headers=headers).json()
       
        # # grab time stamp object
        # pushes, *_ = latest_pushes
        # created, *_ = pushes[0]
        # [Pushbullet API](https://docs.pushbullet.com/v16/#pushes)
        time_stamp = latest_pushes["pushes"][0]["created"]
        image_url =  latest_pushes["pushes"][0]["file_url"]
        last_push_timestap = time_stamp

        print(f"{time_stamp}, {last_push_timestap}, {image_url}")
        print(latest_pushes)
        mardown_formated_image = f"![created with www.github.com/wisehackermonkey/markdown-image-clipboard]({image_url})"
        pyperclip.copy(mardown_formated_image)


        
            

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        while True:
            if stop == 1:   
                break
            time.sleep(1)
            # ws.send("Hello %d" % i)
            print("waiting..")
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


app.mainloop()
# def start_websocket_client():


# if __name__ == "__main__":

    
# import tkinter as tk
# import threading
# import sys
# import os
# class App(threading.Thread):

#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.start()

#     def close_window(self):
#         self.root.quit()

#     def play_tts(self):
#         print("Playing")

#     def restart(self):
#         """Restarts the current program.
#         Note: this function does not return. Any cleanup action (like
#         saving data) must be done before calling this function."""
#         print("Stopping")
#         python = sys.executable
#         os.execl(python, python, * sys.argv)

#     def run(self):
#         self.root = tk.Tk()

#         # start application minimized
#         self.root.iconify()

#         # set window name 
#         self.root.title("Markdown Image Clipboard (pushbullet)")

#         #set minimum window size
#         self.root.minsize(400,100)

#         # setup quit callback on windows close
#         self.root.protocol("WM_DELETE_WINDOW", self.close_window)
       

#         # Title text
#         label = tk.Label(self.root, text="Markdown Image Clipboard (pushbullet)")
#         label.pack()

#         # TODO add pause button

#         # Stop button
#         button = tk.Button(self.root, justify="center", text="Stop", command=self.restart)
#         button.pack()


#         # Update app button
#         self.menubar = tk.Menu(self.root)

#         self.filemenu = tk.Menu(self.root,tearoff=0)


#         self.filemenu.add_command(label="Update", command=check_for_update)
#         self.filemenu.add_command(label="Exit", command=self.close_window)

#         self.menubar.add_cascade(label="Options", menu=self.filemenu)


#         # display the menu
#         self.root.config(menu=self.menubar)

#         # Quit button
#         self.quit = tk.Button(self.root, text="Quit", command=self.root.quit)
#         self.quit.pack(side="bottom")

#         # Start of threaded main tkinter loop
#         self.root.mainloop()