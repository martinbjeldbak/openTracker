import requests
import json
from .util import steamID

version = 0.1
rootURL = 'http://127.0.0.1:3000'


def getInitRequestData(ac_version):
    ver = version

    requestData = {
        'ot_version': str(ver),
        'ac_version': str(ac_version),
        'user_agent': 'openTracker',
        'user_id': steamIDtoUserID(steamID())
    }
    return requestData


def steamIDtoUserID(steam_id):
    response = requests.get(rootURL + '/users/search.json',
                            params={'q': steam_id})
    return json.loads(response.text)[0]['id']
