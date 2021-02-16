# this file grabs the image url from pushbullet when the user
# sends it from there phone. im using websockets to grab the data.

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



try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
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


        
            

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(1000):
            time.sleep(1)
            # ws.send("Hello %d" % i)
            print("waiting..")
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(pushbullet_websocket_api_url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
    