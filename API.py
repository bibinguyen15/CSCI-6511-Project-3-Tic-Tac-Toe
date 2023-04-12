import requests
import constants
import json


url = 'https://www.notexponential.com/aip2pgaming/api/index.php'

headers = {
    'User-Agent': 'PostmanRuntime/7.31.3',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'close',
    'x-api-key': '347b85f18bd488493e87',
    'userId': constants.userId,
}

gameId = '4000'


class API:
    def createAGame(boardSize=3, target=3):
        url = "https://www.notexponential.com/aip2pgaming/api/index.php"

        payload = {'type': 'game',
                   'teamId1': constants.teamId,
                   'teamId2': constants.teamId2,
                   'gameType': 'TTT',
                   'boardSize': boardSize,
                   'target': target}

        response = requests.request(
            "POST", url, headers=headers, data=payload)

        gameDetails = json.loads(response.text)
        code, gameId = gameDetails['code'], gameDetails['gameId']
        print(gameDetails)

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

    def makeMove(move):

        url = "https://www.notexponential.com/aip2pgaming/api/index.php"

        payload = {'type': 'move',
                   'gameId': gameId,
                   'teamId': '1349',
                   'move': move}

        response = requests.request(
            "POST", url, headers=headers, data=payload)

        print(response.text)


# API.get_board_string(3724)
#API.makeMove('1, 3')
# API.getBoardString(3724)
API.getBoardString(gameId)
