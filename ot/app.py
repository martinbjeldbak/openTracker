import sys
sys.path.insert(0, 'apps/python/openTracker/DLLs')

import ac
import acsys
import datetime
import threading
from .logger import logger
from .util import getCoords, steamID, eqByMargin
from .session import Session

count = 0


class App:
    def __init__(self, id):
        self.app_id = id

    def onStartup(self, ac_version):
        self.steam_id = steamID()
        self.ac_version = ac_version
        driver = ac.getDriverName(0)
        car = ac.getCarName(0)
        track = ac.getTrackName(0)
        track_config = ac.getTrackConfiguration(0)
        self.session = Session(ac_version, driver, car, track, track_config)
        self.latestPos = getCoords()
        self.latestUpdate = datetime.datetime.now()

    def onShutdown(self):
        self.session.end()

    # This is called on every dt update, used for
    # important stuff that needs to be known right away
    def onUpdate(self, dt):
        2+dt

    # This is not called as often, every 16 ticks
    def updateRaceInfo(self):
        t = threading.Thread(target=self.sendInfo)
        t.start()

    def sendInfo(self):
        now = datetime.datetime.now()
        if not eqByMargin(2, self.latestPos, getCoords()) or (now - self.latestUpdate).seconds > 2:
            self.latestPos = getCoords()
            self.latestUpdate = now
            laps = ac.getCarState(0, acsys.CS.LapCount) + 1
            speed = ac.getCarState(0, acsys.CS.SpeedMS)
            rpm = ac.getCarState(0, acsys.CS.RPM)
            gear = ac.getCarState(0, acsys.CS.Gear)
            on_gas = ac.getCarState(0, acsys.CS.Gas)
            on_brake = ac.getCarState(0, acsys.CS.Brake)
            on_clutch = ac.getCarState(0, acsys.CS.Clutch)
            steer_rot = ac.getCarState(0, acsys.CS.Steer)
            cur_lap_time_ms = ac.getCarState(0, acsys.CS.LapTime)
            performance_meter = ac.getCarState(0, acsys.CS.PerformanceMeter)

            best_lap = ac.getCarState(0, acsys.CS.BestLap)
            last_lap = ac.getCarState(0, acsys.CS.LastLap)

            self.session.setLapNr(laps, last_lap, best_lap)
            self.session.setPosInfo(getCoords(), speed, rpm, gear,
                                    on_gas, on_brake, on_clutch, steer_rot,
                                    cur_lap_time_ms, performance_meter)

ot_app = App(ac.newApp('openTracker'))
