from .logger import Logger


class Lap:
    def __init__(self, sesskey, lapNr=1):
        self.logger = Logger()
        self.sessKey = sesskey
        self.lapNr = lapNr
        # POST a new lap to the server here

    def setLatestPos(self, pos={'x': 0, 'y': 0, 'z': 0}):
        self.latestPos = pos
