from .logger import Logger
from .config import rootURL, curUserID
from .util import sessionAuthHeader, eqByMargin
import json
import requests


class Lap:
    def __init__(self, sesskey, sessID, lapNr=1):
        self.logger = Logger()
        self.sessKey = sesskey
        self.lapNr = lapNr
        self.sessID = sessID
        self.latestPos = {'x': -100, 'y': -100, 'z': -100}

        payload = {'lap': {'lap_nr': self.lapNr}}
        lapResp = requests.post(rootURL + '/users/' + curUserID() + '/race_sessions/' +
                                str(self.sessID) + '/laps.json',
                                data=json.dumps(payload),
                                headers=sessionAuthHeader(self.sessKey))
        self.lapInfo = json.loads(lapResp.text)

    def setPosInfo(self, pos, ms, rpm, gear, on_gas, on_brake, on_clutch,
                   steer_rot):
        if not eqByMargin(2, self.latestPos, pos):
            self.latestPos = pos
            payload = {'position':
                      {'x': pos['x'], 'y': pos['y'], 'z': pos['z'],
                          'speed': ms, 'rpm': rpm, 'gear': gear,
                          'on_gas': on_gas, 'on_brake': on_brake,
                          'on_clutch': on_clutch, 'steer_rot': steer_rot}}
            requests.post(rootURL + '/users/' + curUserID() + '/race_sessions/' + str(self.sessID) +
                          '/laps/' + str(self.lapInfo['id']) + '/positions.json',
                          data=json.dumps(payload),
                          headers=sessionAuthHeader(self.sessKey))
