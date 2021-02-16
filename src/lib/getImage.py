# this file grabs the image url from pushbullet when the user
# sends it from there phone. im using websockets to grab the data.

import os
import json
import time
import requests
import websocket
import pyperclip
from dotenv import load_dotenv


try:
    import thread
except ImportError:
    import _thread as thread

load_dotenv()

# handels communication with pushbullet api to grab image urls when the user posts them using there phone
# and copies them 
class GetImage(self):
    self.is_running = true
    def __init__(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(pushbullet_websocket_api_url,
            on_message = self.on_message,
            on_error = self.on_error,
            on_close = self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

    def listen(self):
        while self.is_running:
            print("working")
    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")
 
    def on_open(self, ws):
        """starts up a sepreate thread that waits for any 
        incoming messages from pushbullet"""
        def run(*args):
            while running:
                time.sleep(1)
                # ws.send("Hello %d" % i)
                print("waiting..")
            time.sleep(1)
            ws.close()
            print("thread terminating...")
            thread.start_new_thread(run, ())
    def on_message(self, ws, message):
        json_message = dict(json.loads(message))
        
        print(f"Message: {message=}")
        
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

            print(f"{time_stamp=}, {last_push_timestap=}, {image_url=}")
            print(latest_pushes)
            mardown_formated_image = f"![created with www.github.com/wisehackermonkey/markdown-image-clipboard]({image_url})"
            pyperclip.copy(mardown_formated_image)


        
