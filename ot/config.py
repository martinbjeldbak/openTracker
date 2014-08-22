import requests
from .util import steamID
from .logger import logger

version = 0.1
#rootURL = 'http://192.168.0.20:3000'
rootURL = 'http://opentracker.herokuapp.com'

__user_id = ""


def curUserID():
    global __user_id
    if(__user_id == ""):
        __user_id = steamIDtoUserID(steamID())
    return __user_id


def steamIDtoUserID(steam_id):
        response = requests.get(rootURL + '/users/search.json',
                                params={'q': steam_id})
        return str(response.json()['users'][0]['id'])
