import time
import requests
import json
from constants import GET_BOARD_STRING, GET_MOVE, POST_API_URL
from Project_3_Cat import TTT

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

class API:
    def getMove(gameId):
        url = GET_MOVE +gameId

        params = {
            'type': 'move',
            'gameId': gameId
        }

        response = requests.request(
            "GET", url, params=params, headers=headers)
        
        moveDetails = json.loads(response.text)
        moveCode, moveId, moveX, moveY = moveDetails['code'], moveDetails['moveId'], moveDetails['moveX'], moveDetails['moveY']
        return moveCode
    
    def createGame( gameId, teamId1, teamId2, boardSize, target):
        if gameId == 0:
            url = POST_API_URL

            payload = {'type':'game',
                   'teamId1': teamId1,
                   'teamId2': teamId2,
                   'gameType': 'TTT',
                   'boardSize': boardSize,
                   'target': target}

            response = requests.request(
            "POST", url, headers=headers, data=payload)
            gameDetails = json.loads(response.text)
            code, gameId = gameDetails['code'], gameDetails['gameId']
            time.sleep(5)
            moveMade = False
            print(gameDetails)
            print(code)
            print(response.text)
        
        else:
            moveMade = True
            url = GET_BOARD_STRING +gameId
            params = {
                 'type': 'boardString',
                 'gameId': gameId
            }
            response = requests.request(
            "GET", url, params=params, headers=headers)
            boardDetails = json.loads(response.text)
            code, boardString = boardDetails['code'], boardDetails['output']
            print(boardString)
            board = TTT()
            board.setBoard(boardDetails['target'], boardDetails['target'])
            if moveMade:
                url = GET_MOVE +gameId
                params = {
                    'type': 'move',
                    'gameId': gameID
                }
                response = requests.request("GET", url, params=params, headers=headers)
                moveDetails = json.loads(response.text)
                moveCode, moveId, moveX, moveY = moveDetails['code'], moveDetails['moveId'], moveDetails['moveX'], moveDetails['moveY']
                while moveCode == 'FAIL':
                    time.sleep(1)
                    print("No move made")
                
    def getBoardString(gameID):
        url = GET_BOARD_STRING +gameId

        params = {
            'type': 'boardString',
            'gameId': gameID
        }

        response = requests.request(
            "GET", url, params=params, headers=headers)

        return response.text

    def makeMove(move, id):

        url = POST_API_URL

        payload = {'type': 'move',
                   'gameId': id,
                   'teamId': '1349',
                   'move': move}

        response = requests.request(
            "POST", url, headers=headers, data=payload)

        print(response.text)
    
