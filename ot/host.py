import requests


class Host:
    def __init__(self):
        self.url = "http://127.0.0.1:1337"

    def put(self, data):
        r = requests.put(self.url, data)
