from ot.app import app
from ot.logger import Logger

updateError = False
logger = Logger()


def acMain(ac_version):
    global logger

    logger.debug("Starting OpenTracker")

    try:
        logger.logToAC('Hello from openTracker')
        app.onStartup()
    except Exception as e:
        logger.logToAC('Opentracker exception')
        logger.exception('Error in openTracker onStartup: ' % e)

    return "OpenTracker"


def acUpdate(dt):
    global updateError, logger

    if updateError:
        return

    try:
        return -1
        #app.onUpdate(dt)
    except Exception as e:
        updateError = True
        logger.exception('Error in openTracker onUpdate: ' % e)


def acShutdown():
    app.onShutdown()
    logger.logToAC('Successfully shut down')
