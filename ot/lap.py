from .logger import Logger
from .config import rootURL, curUserID
from .util import sessionAuthHeader 
import json
import requests


class Lap:
    def __init__(self, sesskey, sessID, lapNr=1, last_lap_ms=0, best_lap_ms=-1):
        self.logger = Logger()
        self.sessKey = sesskey
        self.lapNr = lapNr
        self.sessID = sessID
        self.latestPos = {'x': -1000, 'y': -1000, 'z': -1000}
        self.logger.debug("SUP")
        payload = {'lap': {'lap_nr': self.lapNr, 'last_lap': last_lap_ms,
                           'best_lap': best_lap_ms}}

        lapResp = requests.post(rootURL + '/users/' + curUserID() + '/race_sessions/' +
                                str(self.sessID) + '/laps.json',
                                data=json.dumps(payload),
                                headers=sessionAuthHeader(self.sessKey))
        self.lapInfo = json.loads(lapResp.text)['lap']

    def setPosInfo(self, pos, ms, rpm, gear, on_gas, on_brake, on_clutch,
                   steer_rot, cur_lap_time, performance_meter):
        self.latestPos = pos
        payload = {'position':
                  {'x': pos['x'], 'y': pos['y'], 'z': pos['z'],
                   'speed': ms, 'rpm': rpm, 'gear': gear,
                   'on_gas': on_gas, 'on_brake': on_brake,
                   'on_clutch': on_clutch, 'steer_rot': steer_rot,
                   'lap_time': cur_lap_time,
                   'performance_meter': performance_meter}}
        requests.post(rootURL + '/users/' + curUserID() + '/race_sessions/' + str(self.sessID) +
                      '/laps/' + str(self.lapInfo['id']) + '/positions.json',
                      data=json.dumps(payload),
                      headers=sessionAuthHeader(self.sessKey))
