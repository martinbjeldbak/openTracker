import ac
from .logger import Logger
#from .util import getCoords, steamID
#from .ot import Host

count = 0


class App:
    def __init__(self, id):
        self.app_id = id
        self.logger = Logger()
        #self.site = Host()

    def onStartup(self):
        self.logger.debug('Hello, testing from opentracker')
        #self.steam_id = steamID()

    def onShutdown(self):
        self.logger.debug('OpenTracker successfully shutdown')

    def onUpdate(self, dt):
        global count

        if (count >= 1000):
            count = 0
        count = count + 1

        #self.site.put(getCoords())


app = App(ac.newApp('openTracker'))
