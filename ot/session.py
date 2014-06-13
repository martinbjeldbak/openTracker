from .logger import Logger
from .lap import Lap
from .config import getInitRequestData, rootURL
import json
import requests


class Session:
    def __init__(self, ac_version):
        self.logger = Logger()

        payload = {'session': getInitRequestData(ac_version)}
        headers = {'content-type': 'application/json'}
        self.newSessResp = requests.post(rootURL + '/api/v1/sessions',
                                         data=json.dumps(payload),
                                         headers=headers)
        self.sessKey = json.loads(self.newSessResp.text)['key']['key']
        self.currentLap = 1
        self.laps = [Lap(self.sessKey, self.currentLap)]

    def getLatestLap(self):
        return self.laps[-1]

    def setLapNr(self, lapNr):
        if self.currentLap < lapNr:
            self.currentLap = lapNr
            self.laps.append(Lap(self.sessKey, self.currentLap))

    def setCoords(self, coords):
        self.getLatestLap().setLatestPos(coords)
