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
        self.session = Session()

    def onStartup(self):
        self.steam_id = steamID()

    def onShutdown(self):
        self.logger.debug('OpenTracker successfully shutdown')

    def onUpdate(self, dt):
        global count

        count = count + 1

        if (count >= 1000):
            #self.site.put(getCoords())
            count = 0


app = App(ac.newApp('openTracker'))
