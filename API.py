import requests
import constants
import json
from constants import *

url = 'https://www.notexponential.com/aip2pgaming/api/index.php'

headers = {
    'User-Agent': 'PostmanRuntime/7.31.3',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'close',
    'x-api-key': xapikey,
    'userId': constants.userId,
}

gameId = '4000'
teamId = constants.teamId


def getMoves(gameId, count=1):
    url = constants.GET_MOVES + str(gameId) + "&count=" + str(count)

    params = {
        'type': 'moves',
        'gameId': gameId,
        'count': count
    }
    response = requests.request(
        "GET", url, params=params, headers=headers)

    jsonData = json.loads(response.text)

    if jsonData['code'] == 'FAIL':
        return 'FAIL'
    else:
        moveDetails = jsonData["moves"][0]

    return {'teamId': moveDetails['teamId'],
            'x': int(moveDetails['moveX']), 'y': int(moveDetails['moveY'])}


def createAGame(teamId2, boardSize=5, target=5):
    url = "https://www.notexponential.com/aip2pgaming/api/index.php"

    payload = {'type': 'game',
               'teamId1': constants.teamId,
               'teamId2': teamId2,
               'gameType': 'TTT',
               'boardSize': boardSize,
               'target': target}

    response = requests.request(
        "POST", url, headers=headers, data=payload)

    gameDetails = json.loads(response.text)
    code, gameId = gameDetails['code'], gameDetails['gameId']

    if code == 'FAIL':
        return code

    return gameId


def getBoardString(gameID):
    url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=boardString&gameId=3724"

    payload = {}

    params = {
        'type': 'boardString',
        'gameId': gameID
    }

    response = requests.request(
        "GET", url, params=params, headers=headers, data=payload)

    strMap = json.loads(response.text)
    print(strMap)
    board, target = strMap['output'], strMap['target']

    return board, target


'''
def makeMove(move):

    url = "https://www.notexponential.com/aip2pgaming/api/index.php"

    payload = {'type': 'move',
               'gameId': gameId,
               'teamId': teamId,
               'move': move}

    response = requests.request(
        "POST", url, headers=headers, data=payload)

    moveDetails = json.loads(response.text)
    return moveDetails
'''


def makeMove(move, gameId):
    url = POST_API_URL

    print("Game id passed in:", gameId, type(gameId))

    payload = {'type': 'move',
               'gameId': gameId,
               'teamId': teamId,
               'move': move}

    response = requests.request(
        "POST", url, headers=headers, data=payload)

    moveDetails = json.loads(response.text)
    print(moveDetails)
    return moveDetails


# API.get_board_string(3724)
# API.makeMove('1, 3')
# API.getBoardString(3724)
# getBoardString(gameId)
# print(getMoves('4134', 4))

# makeMove('2,3', '4134')


