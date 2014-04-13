from .util import steamID

version = 0.1


def getInitRequestData():
    ver = version

    requestData = {
        'version': str(ver),
        'user_agent': 'openTracker',
        'steam_id': steamID()
    }
    return requestData
