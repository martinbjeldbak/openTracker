import sys
sys.path.insert(0, 'apps/python/openTracker/DLLs')

import ac
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
        self.logger.debug('OpenTracker successfully shutdown')

    def onUpdate(self, dt):
        global count

        count = count + 1

        if (count >= 1000):
            #self.site.put(getCoords())
            count = 0


app = App(ac.newApp('openTracker'))
