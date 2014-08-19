from .logger import Logger
from .lap import Lap
from .config import version, rootURL, curUserID
from .util import sessionAuthHeader
import json
import requests
from time import gmtime, strftime


class Session:
    def __init__(self, ac_version, driver, car, track, track_config):
        self.logger = Logger()

        payload = {'race_session': {'ot_version': str(version),
                   'user_agent': 'openTracker', 'ac_version': str(ac_version),
                   'driver': driver, 'car': car},
                   'track': {'track': track,
                             'track_config': track_config
                             }
                   }
        headers = {'content-type': 'application/json'}
        self.logger.debug(rootURL + '/users/' + curUserID() + '/race_sessions.json')
        newSessResp = requests.post(rootURL + '/users/' + curUserID() + '/race_sessions.json',
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
        payload = {'race_session': {'ended_at': strftime(
                                    "%a, %d %b %Y %X +0000", gmtime())}}
        requests.put(rootURL + '/users/' + curUserID() + '/race_sessions/' +
                     str(self.session['id']) + ".json",
                     data=json.dumps(payload),
                     headers=sessionAuthHeader(self.sessKey))

    def getLatestLap(self):
        return self.laps[-1]

    def setLapNr(self, lapNr=1, last_lap_ms=0, best_lap_ms=0):
        if self.currentLap < lapNr:
            self.currentLap = lapNr
            self.laps.append(Lap(self.sessKey, self.sessID,
                                 self.currentLap, last_lap_ms, best_lap_ms))

    def setPosInfo(self, coords, speed, rpm, gear, on_gas, on_brake,
                   on_clutch, steer_rot, cur_lap_time, performance_meter):
        self.getLatestLap().setPosInfo(coords, speed, rpm, gear, on_gas,
                                       on_brake, on_clutch, steer_rot,
                                       cur_lap_time, performance_meter)
