import ac
import acsys
import steam_info


def getCoords():
    x, y, z = ac.getCarState(0, acsys.CS.WorldPosition)
    return dict(x=x, y=y, z=z)


def steamID():
    return ""
    #return steam_info.get_steam_id()
