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
