import sys
sys.path.insert(0, 'apps/python/openTracker/DLLs')

import ac
import acsys
from .logger import Logger
from .util import getCoords, steamID
from .session import Session

count = 0


class App:
    def __init__(self, id):
        self.app_id = id
        self.logger = Logger()

    def onStartup(self, ac_version):
        self.steam_id = steamID()
        self.ac_version = ac_version
        self.session = Session(ac_version)

    def onShutdown(self):
        self.session.end()

    # This is called on every dt update, used for
    # important stuff that needs to be known right away
    def onUpdate(self, dt):
        2+dt

    # This is not called as often, every 16 ticks
    def updateRaceInfo(self):
        cur_laps = ac.getCarState(0, acsys.CS.LapCount) + 1
        self.session.setLapNr(cur_laps)
        self.session.setCoords(getCoords())

app = App(ac.newApp('openTracker'))
