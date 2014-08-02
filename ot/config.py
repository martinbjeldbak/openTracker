import requests
from .util import steamID
from .logger import Logger

version = 0.1
rootURL = 'http://127.0.0.1:3000'

__user_id = ""


def getInitRequestData(ac_version):
    ver = version

    requestData = {
        'ot_version': str(ver),
        'ac_version': str(ac_version),
        'user_agent': 'openTracker',
        'user_id': curUserID()
    }
    return requestData


def curUserID():
    global __user_id
    if(__user_id == ""):
        __user_id = steamIDtoUserID(steamID())
    return __user_id


def steamIDtoUserID(steam_id):
        response = requests.get(rootURL + '/users/search.json',
                                params={'q': steam_id})
        return str(response.json()['users'][0]['id'])
