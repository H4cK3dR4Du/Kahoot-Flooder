import os, re, sys, time, json, base64, random, string, ctypes, getpass, threading

try:
    import requests
    import uuid
    import datetime
    import colorama
    import pystyle
    import websocket
    import py_mini_racer
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install uuid")
    os.system("pip install datetime")
    os.system("pip install colorama")
    os.system("pip install pystyle")
    os.system("pip install websocket-client")
    os.system("pip install py_mini_racer")

from pystyle import Write, System, Colors, Colorate, Center
from colorama import Fore, Style, init
from datetime import datetime

class Output:
    def colored_text(hex_color):
        ansi_color = f"\033[38;2;{int(hex_color[1:3], 16)};{int(hex_color[3:5], 16)};{int(hex_color[5:], 16)}m"

        return ansi_color
    
    reset = colored_text("#ffffff")
    red = colored_text("#c1121f")
    pink = colored_text("#ffafcc")
    medium_dark_green = colored_text("#4f772d")
    dark_green = colored_text("#606c38")
    light_cyan = colored_text("#3bceac")
    green = colored_text("#70e000")
    magenta = colored_text("#662e9b")
    idk = colored_text("#ee6c4d")
    yellow = colored_text("#f0c808")
    strong_red = colored_text("#660708")
    gray = colored_text("#5f7470")
    light_blue = colored_text("#baf2d8")
    light_green = colored_text("#8ea604")
    cherry = colored_text("#b23a48")
    light_magenta = colored_text("#a663cc")
    dark_blue = colored_text("#0d00a4")
    pretty_green = colored_text("#9ef01a")
    turquesa = colored_text("#00916e")
    orange = colored_text("#f77f00")

class Console:
    def title():
        while Stats.working:
            elapsed_time = time.time() - Stats.start
            elapsed_days = int(elapsed_time // 86400)
            elapsed_hours = int((elapsed_time % 86400) // 3600)
            elapsed_minutes = int((elapsed_time % 3600) // 60)
            elapsed_seconds = int(elapsed_time % 60)

            ctypes.windll.kernel32.SetConsoleTitleW(f'𝓚𝓪𝓱𝓸𝓸𝓽 𝓕𝓵𝓸𝓸𝓭𝓮𝓻 | 𝓢𝓾𝓬𝓬𝓮𝓼𝓼: {Stats.flooded} - 𝓕𝓪𝓲𝓵𝓮𝓭: {Stats.failed} - 𝓔𝓵𝓪𝓹𝓼𝓮𝓭: {elapsed_days}𝓭 {elapsed_hours}𝓱 {elapsed_minutes}𝓶 {elapsed_seconds}𝓼 | .𝓰𝓰/𝓻𝓪𝓭𝓾𝓬𝓸𝓻𝓭')

class Stats:
    flooded = 0
    failed = 0
    start = time.time()
    working = True

class Websockets:
    def __init__(self) -> None:
        pass

    def __connect__(self) -> dict:
        return [
            {
                "id": "1",
                "version": "1.0",
                "minimumVersion": "1.0",
                "channel": "/meta/handshake",
                "supportedConnectionTypes": [
                    "websocket",
                    "long-polling",
                    "callback-polling"
                ],
                "advice": {
                    "timeout": 60000,
                    "interval": 0
                },
                "ext": {
                    "ack": True,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": 0,
                        "o": 0
                    }
                }
            }
        ]
    
    def __clientId__(self, clientId) -> dict:
        return [
            {
                "id": 2,
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "advice": {
                    "timeout": 0
                },
                "clientId": clientId,
                "ext": {
                    "ack": 0,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]
    
    def __clientId2__(self, clientId) -> dict:
        return [
            {
                "id": "3",
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "clientId": clientId,
                "ext": {
                    "ack": 1,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]
    
    def __connectID__(self, clientId, gameId, name) -> dict:
        return [
            {
                "channel": "/service/controller",
                "clientId": clientId,
                "data": {
                    "content": "{\"device\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0\",\"screen\":{\"width\":920,\"height\":974}}}",
                    "gameid": gameId,
                    "host": "kahoot.it",
                    "name": name,
                    "type": "login"
                },
                "ext": {},
                "id": "4"
            }
        ]
    
    def __keepInGame__(self, clientId, gameId) -> dict:
        return [
            {
                "id": "5",
                "channel": "/service/controller",
                "clientId": clientId,
                "data": {
                    "content": "{\"usingNamerator\":false}",
                    "gameid": gameId,
                    "host": "kahoot.it",
                    "id": 16,
                    "type": "message"
                },
                "ext": {}
            }
        ]
    
    def __metaConnect__(self, clientId) -> dict:
        return [
            {
                "id": "6",
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "clientId": clientId,
                "ext": {
                    "ack": 2,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]
    
    def __ezFlooder__(self, clientId, id, ack) -> dict:
        return [
            {
                "id": id,
                "channel": "/meta/connect",
                "connectionType": "websocket",
                "clientId": clientId,
                "ext": {
                    "ack": ack,
                    "timesync": {
                        "tc": str(time.time()),
                        "l": random.randint(100, 999),
                        "o": random.randint(-999, -100)
                    }
                }
            }
        ]

class Solver:
    def __init__(self, challenge, token) -> None:
        self.challenge = challenge
        self.session_token = token

    def __xorStrings__(self, challenge, token) -> str:
        result = ""
        for c1, c2 in zip(challenge, base64.b64decode(token).decode('utf-8', 'strict')):
            result += chr(ord(c1) ^ ord(c2))

        return result

    def __solve__(self) -> str:
        text = re.split("[{};]", self.challenge.encode('ascii', 'ignore').decode('utf-8').replace('\t', '', -1))
        js_code = [text[1] + "{", text[2] + ";", "return message.replace(/./g, function(char, position) {", text[7] + ";})};", text[0]]
        js = py_mini_racer.MiniRacer()
        solved = js.eval("".join(js_code))
        return self.__xorStrings__(solved, self.session_token)

class KahootFlooder:
    def __init__(self, id, name) -> None:
        self.kahoot_id = id
        self.bot_names = name

        self.ack = 2
        self.id = 6

    def __time__(self) -> str:
        return "{:%H:%M:%S}".format(datetime.now())

    def __flood__(self) -> None:
        try:
            cookies = {
                "generated_uuid": str(uuid.uuid4()),
                "player": "active"
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
            }

            r = requests.get(f'https://kahoot.it/reserve/session/{self.kahoot_id}/?{time.time()}', headers=headers, cookies=cookies)
            
            start = time.time()

            challenge = Solver(
                challenge=r.json()["challenge"],
                token=r.headers["X-Kahoot-Session-Token"]
            ).__solve__()

            elapsed_time = time.time() - start
            print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.light_blue}${Output.reset}) {Output.gray}Solved Challenge: {Output.light_cyan}{challenge[:60]}******** {Output.reset}In {elapsed_time:.2f}s")
            
            wsocket = websocket.create_connection(f'wss://kahoot.it/cometd/{self.kahoot_id}/{challenge}')
            wsocket.send(json.dumps(Websockets.__connect__(self)))
            cid = json.loads(wsocket.recv())[0]["clientId"]

            wsocket.send(json.dumps(Websockets.__clientId__(self, cid)))
            wsocket.recv()

            wsocket.send(json.dumps(Websockets.__clientId2__(self, cid)))

            success = False
            while not success:
                name = f"{self.bot_names}_{random.randint(999999, 9999999)}"
                wsocket.send(json.dumps(Websockets.__connectID__(self, cid, self.kahoot_id, name)))
                print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.magenta}^{Output.reset}) {Output.magenta}Connected To Websocket: {Output.light_cyan}{name} {Output.reset}[{Output.orange}{cid}{Output.reset}]")
                if '"loginResponse","cid":' in wsocket.recv():
                    print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.green}+{Output.reset}) {Output.green}Successfully Joined: {Output.light_cyan}{name}")
                    Stats.flooded += 1
                    success = True

            wsocket.send(json.dumps(Websockets.__keepInGame__(self, cid, self.kahoot_id)))
            wsocket.send(json.dumps(Websockets.__metaConnect__(self, cid)))

            while True:
                self.id += 1
                self.ack += 1

                wsocket.send(json.dumps(Websockets.__ezFlooder__(self, cid, self.id, self.ack)))
                wsocket.recv()
            
        except:
            print(f"{Output.gray} {self.__time__()} {Output.reset}({Output.strong_red}!{Output.reset}) {Output.red}ERROR: Failed To Connect Websocket.")
            Stats.failed += 1

if __name__ == "__main__":
    try:
        Write.Print(f'''
\t\t88888888ba                        88               88                                             
\t\t88      "8b                       88               88                                      ,d     
\t\t88      ,8P                       88               88                                      88     
\t\t88aaaaaa8P'  ,adPPYYba,   ,adPPYb,88  88       88  88,dPPYba,    ,adPPYba,    ,adPPYba,  MM88MMM  
\t\t88""""88'    ""     `Y8  a8"    `Y88  88       88  88P'    "8a  a8"     "8a  a8"     "8a   88     
\t\t88    `8b    ,adPPPPP88  8b       88  88       88  88       88  8b       d8  8b       d8   88     
\t\t88     `8b   88,    ,88  "8a,   ,d88  "8a,   ,a88  88       88  "8a,   ,a8"  "8a,   ,a8"   88,    
\t\t88      `8b  `"8bbdP"Y8   `"8bbdP"Y8   `"YbbdP'Y8  88       88   `"YbbdP"'    `"YbbdP"'    "Y888\n''', Colors.purple_to_red, interval=0.000)
        line = f"{Output.cherry}={Output.red}="
        print(line * 60)

        threading.Thread(target=Console.title).start()

        threads = input(f"\n{Output.gray} {KahootFlooder.__time__("")} {Output.reset}({Output.cherry}?{Output.reset}) {Output.gray}Bot Amount: {Output.light_cyan}")
        names = input(f"{Output.gray} {KahootFlooder.__time__("")} {Output.reset}({Output.cherry}?{Output.reset}) {Output.gray}Bot Names: {Output.light_cyan}")
        kahoot_id = input(f"{Output.gray} {KahootFlooder.__time__("")} {Output.reset}({Output.cherry}?{Output.reset}) {Output.gray}Kahoot Game ID: {Output.light_cyan}"); print()

        while True:
            while threading.active_count()-1 < int(threads) + 1:
                kahoot = KahootFlooder(
                    id = kahoot_id,
                    name = names
                )
                threading.Thread(target=kahoot.__flood__).start()
            time.sleep(1)
    except:
        pass
