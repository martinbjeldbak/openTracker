from .logger import Logger
from .lap import Lap
from .config import getInitRequestData, rootURL
import json
import requests
from time import gmtime, strftime


class Session:
    def __init__(self, ac_version):
        self.logger = Logger()

        payload = {'session': getInitRequestData(ac_version)}
        headers = {'content-type': 'application/json'}
        self.newSessResp = requests.post(rootURL + '/api/v1/sessions',
                                         data=json.dumps(payload),
                                         headers=headers)
        self.session = json.loads(self.newSessResp.text)
        self.sessKey = self.session['key']['key']

        # Set initial lap info
        self.currentLap = 1
        self.laps = [Lap(self.sessKey, self.currentLap)]

    def end(self):
        payload = {'session': {'ended_at': strftime("%a, %d %b %Y %X +0000", gmtime())}}

        headers = {'content-type': 'application/json',
                   'AUTHORIZATION': 'Token token="' + self.sessKey + '"'}
        requests.put(rootURL + '/api/v1/sessions/' + str(self.session['id']),
                     data=json.dumps(payload),
                     headers=headers)

    def getLatestLap(self):
        return self.laps[-1]

    def setLapNr(self, lapNr):
        if self.currentLap < lapNr:
            self.currentLap = lapNr
            self.laps.append(Lap(self.sessKey, self.currentLap))

    def setCoords(self, coords):
        self.getLatestLap().setLatestPos(coords)
