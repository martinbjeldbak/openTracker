from .logger import Logger
from .config import rootURL
from .util import sessionAuthHeader, eqByMargin
import json
import requests


class Lap:
    def __init__(self, sesskey, sessID, lapNr=1):
        self.logger = Logger()
        self.sessKey = sesskey
        self.lapNr = lapNr
        self.sessID = sessID
        self.latestPos = {'x': 0, 'y': 0, 'z': 0}

        payload = {'lap': {'lap_nr': self.lapNr}}
        lapResp = requests.post(rootURL + '/api/v1/sessions/' + str(self.sessID) + '/laps',
                                data=json.dumps(payload),
                                headers=sessionAuthHeader(self.sessKey))
        self.logger.debug(lapResp.text)
        self.lapInfo = json.loads(lapResp.text)

    def setLatestPos(self, pos={'x': 0, 'y': 0, 'z': 0}):
        if not eqByMargin(2, self.latestPos, pos):
            self.latestPos = pos
            payload = {'position': self.latestPos}
            requests.post(rootURL + '/api/v1/sessions/' + str(self.sessID) +
                          '/laps/' + str(self.lapInfo['id']) + '/positions/',
                          data=json.dumps(payload),
                          headers=sessionAuthHeader(self.sessKey))
