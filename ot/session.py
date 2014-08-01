from .logger import Logger
from .lap import Lap
from .config import getInitRequestData, rootURL
from .util import sessionAuthHeader
import json
import requests
from time import gmtime, strftime


class Session:
    def __init__(self, ac_version):
        self.logger = Logger()

        payload = {'session': getInitRequestData(ac_version)}
        headers = {'content-type': 'application/json'}
        newSessResp = requests.post(rootURL + '/api/v1/race_sessions',
                                    data=json.dumps(payload),
                                    headers=headers)
        self.session = newSessResp.json()['race_session']
        self.sessKey = self.session['key']
        self.sessID = self.session['id']

        # Set initial lap info
        self.currentLap = float('-inf')
        self.laps = []
        self.setLapNr(1)

    def end(self):
        payload = {'session': {'ended_at': strftime("%a, %d %b %Y %X +0000",
                                                    gmtime())}}
        requests.put(rootURL + '/api/v1/race_sessions/' + str(self.session['id']),
                     data=json.dumps(payload),
                     headers=sessionAuthHeader(self.sessKey))

    def getLatestLap(self):
        return self.laps[-1]

    def setLapNr(self, lapNr):
        if self.currentLap < lapNr:
            self.currentLap = lapNr
            self.laps.append(Lap(self.sessKey, self.sessID, self.currentLap))

    def setPosInfo(self, coords, speed, rpm, gear, on_gas, on_brake,
                   on_clutch, steer_rot):
        self.getLatestLap().setPosInfo(coords, speed, rpm, gear, on_gas,
                                       on_brake, on_clutch, steer_rot)
