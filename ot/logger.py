import logging
import ac
from datetime import datetime
from os import makedirs
from os.path import dirname, realpath, exists


class Logger:
    def __init__(self):
        dir = dirname(dirname(realpath(__file__))) + '/logs'

        if not exists(dir):
            makedirs(dir)

        logging.basicConfig(level=logging.DEBUG, filename=
                            dir + '/OpenTracker.log', filemode='w')
        self.logger = logging.getLogger('OpenTracker')

    def info(self, msg):
        self.logger.info(self._ppMsg(msg))

    def warning(self, msg):
        self.logger.warning(self._ppMsg(msg))

    def debug(self, msg):
        self.logger.debug(self._ppMsg(msg))

    def exception(self, msg):
        self.logger.critical(self._ppMsg(msg))

    def log(self, lvl, msg):
        self.logger.log(lvl, self._ppMsg(msg))

    def error(self, msg):
        self.logger.error(self._ppMsg(msg))

    def logToAC(self, msg):
        ac.log('openTracker: ' + msg)

    def _ppMsg(self, msg):
        return " {0!s}: {1}".format(datetime.now(), msg)
logger = Logger()
