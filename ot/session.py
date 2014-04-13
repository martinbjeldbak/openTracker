from .logger import Logger
from .config import getInitRequestData
import json
import requests


class Session:
    def __init__(self):
        self.url = 'http://127.0.0.1:3000'
        self.logger = Logger()
        # Send initial POST request
        payload = {'session': getInitRequestData()}
        headers = {'content-type': 'application/json'}
        self.logger.info(payload)
        self.sessionToken = requests.post(self.url + '/api/v1/sessions',
                                          data=json.dumps(payload),
                                          headers=headers)
        self.logger.info(self.sessionToken)
    #def new_lap
    #def new_point(x, y, z)
