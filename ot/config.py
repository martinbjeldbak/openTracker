import requests
from .util import steamID
from .logger import logger

version = 1.0
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
