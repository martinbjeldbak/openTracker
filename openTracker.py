from ot.app import app
from ot.logger import Logger

logger = Logger()
ticks = 0


def acMain(ac_version):
    global logger

    logger.info("Starting OpenTracker")

    try:
        logger.logToAC('Hello from openTracker')
        app.onStartup(ac_version)
    except Exception as e:
        logger.logToAC('Opentracker exception')
        logger.exception('Error in openTracker onStartup: ' % e)

    return "OpenTracker"


def acUpdate(dt):
    global logger, ticks
    ticks += 1

    app.onUpdate(dt)

    if ticks >= 16:
        app.updateRaceInfo()
        ticks = 0


def acShutdown():
    app.onShutdown()
    logger.info('OpenTracker successfully shutdown')
    logger.logToAC('Successfully shut down')
