import ac
import acsys
from .logger import Logger


class App:
    def __init__(self, id):
        self.app_id = id
        self.logger = Logger()

    def onStartup(self):
        self.logger.debug('Hello, testing from opentracker')

    def onShutdown(self):
        self.logger.debug('OpenTracker successfully shutdown')

    def onUpdate(self, dt):
        return None

    def getCoords():
        x = ac.getCarState(0, acsys.CS.WorldPosition)[0]
        y = ac.getCarState(0, acsys.CS.WorldPosition)[1]
        z = ac.getCarState(0, acsys.CS.WorldPosition)[2]
        #return {'x': x, 'y': y, 'z': z}
        return dict(x=x, y=y, z=z)
        #return None

app = App(ac.newApp('openTracker'))
