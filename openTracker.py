from ot.app import ot_app
from ot.logger import logger as ot_logger

ot_ticks = 0


def acMain(ac_version):
    ot_logger.info("Starting OpenTracker")

    try:
        ot_logger.logToAC('Hello from openTracker')
        ot_app.onStartup(ac_version)
    except Exception as e:
        ot_logger.logToAC('Opentracker exception')
        ot_logger.exception('Error in openTracker onStartup: ' % e)

    return "OpenTracker"


def acUpdate(dt):
    global ot_ticks
    ot_ticks += 1

    ot_app.onUpdate(dt)

    if ot_ticks >= 16:
        ot_app.updateRaceInfo()
        ot_ticks = 0


def acShutdown():
    ot_app.onShutdown()
    ot_logger.info('OpenTracker successfully shutdown')
    ot_logger.logToAC('Successfully shut down')
