import logging
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

    def debug(self, msg):
        self.logger.debug(msg)
