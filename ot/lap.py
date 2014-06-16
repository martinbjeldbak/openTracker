from .logger import Logger
from .config import rootURL
from .util import sessionAuthHeader
import json
import requests


class Lap:
    def __init__(self, sesskey, sessID, lapNr=1):
        self.logger = Logger()
        self.sessKey = sesskey
        self.lapNr = lapNr
        self.sessID = sessID

        payload = {'lap': {'lap_nr': self.lapNr}}
        self.lapResp = requests.post(rootURL + '/api/v1/sessions/' + str(self.sessID) + '/laps',
                                     data=json.dumps(payload),
                                     headers=sessionAuthHeader(self.sessKey))

    def setLatestPos(self, pos={'x': 0, 'y': 0, 'z': 0}):
        self.latestPos = pos
        payload = {'position': pos}
        #requests.post(rootURL + '/api/v1/sessions/' + str(self.sessID) + '/laps',
        #        data=json.dumps(payload),
        #        headers=sessionAuthHeader(self.sessKey))
