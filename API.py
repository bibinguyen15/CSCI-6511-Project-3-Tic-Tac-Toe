import requests
import json
from constants import teamId, GET_BOARD_STRING, GET_MOVE, POST_API_URL

# print(GET_BOARD_STRING)

headers = {
    'User-Agent': 'PostmanRuntime/7.31.3',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'close',
    'x-api-key': '9922dd6bd436044b109b',
    'userId': '1163',
}

# gameId = '3975'

def getMove(gameId, count):
    url = GET_MOVE +str(gameId)

    params = {
         'type': 'moves',
         'gameId': gameId,
         'count': count
         }
    response = requests.request(
            "GET", url, params=params, headers=headers)
    jsonData = json.loads(response.text)
    moveDetails = jsonData["moves"][0]
    # moveCode, moveId, moveX, moveY = moveDetails['code'], moveDetails['moveId'], moveDetails['moveX'], moveDetails['moveY']
    return {"moveId": moveDetails["moveId"], "x": int(moveDetails["moveX"]), "y": int(moveDetails["moveY"])}
    
def createGame( gameId, teamId2, boardSize, target):
    url = POST_API_URL
    payload = {'type':'game',
               'teamId1': teamId,
               'teamId2': teamId2,
               'gameType': 'TTT',
               'boardSize': boardSize,
               'target': target}
    response = requests.request(
            "POST", url, headers=headers, data=payload)
    gameDetails = json.loads(response.text)
    code, gameId = gameDetails['code'], gameDetails['gameId']
    return gameId
                
def getBoardString(gameId):
    url = GET_BOARD_STRING +str(gameId)
    params = {
        'type': 'boardString',
        'gameId': gameId
        }
    response = requests.request("GET", url, params=params, headers=headers)
    boardDetails = json.loads(response.text)
    # moveCode, moveId, moveX, moveY = moveDetails['code'], moveDetails['moveId'], moveDetails['moveX'], moveDetails['moveY']
    return boardDetails

def makeMove(move, id):
    url = POST_API_URL
    payload = {'type': 'move',
               'gameId': id,
               'teamId': teamId,
               'move': move}

    response = requests.request(
            "POST", url, headers=headers, data=payload)

    moveDetails = json.loads(response.text)
    return moveDetails
    
