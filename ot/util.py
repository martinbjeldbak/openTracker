import ac
import acsys

from steam_info.steam_info import get_steam_username, get_steam_id


def getCoords():
    x, y, z = ac.getCarState(0, acsys.CS.WorldPosition)
    return dict(x=x, y=y, z=z)


def steamID():
    return str(get_steam_id())


def steamUser():
    return get_steam_username()


def sessionAuthHeader(key):
    return {'content-type': 'application/json',
            'AUTHORIZATION': 'Token token="' + key + '"'}


def eqByMargin(margin,
               firstPos={'x': 0, 'y': 0, 'z': 0},
               secondPos={'x': 0, 'y': 0, 'z': 0}):
    isXEq = round(firstPos['x'], margin) == round(secondPos['x'], margin)
    isYEq = round(firstPos['y'], margin) == round(secondPos['y'], margin)
    isZEq = round(firstPos['z'], margin) == round(secondPos['z'], margin)

    if isXEq and isYEq and isZEq:
        return True
    return False
