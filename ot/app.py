import ac
from .logger import Logger
from .util import getCoords, steamID
#from .ot import Host

count = 0


class App:
    def __init__(self, id):
        self.app_id = id
        self.logger = Logger()
        #self.site = Host()

    def onStartup(self):
        self.steam_id = steamID()
        self.logger.debug(self.steam_id)

    def onShutdown(self):
        self.logger.debug('OpenTracker successfully shutdown')

    def onUpdate(self, dt):
        global count

        count = count + 1

        if (count >= 1000):
            count = 0

        #self.site.put(getCoords())


app = App(ac.newApp('openTracker'))
