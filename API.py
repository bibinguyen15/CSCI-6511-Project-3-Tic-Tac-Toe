import requests


url = 'https://www.notexponential.com/aip2pgaming/api/index.php'

headers = {
    'User-Agent': 'PostmanRuntime/7.31.3',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'close',
    'x-api-key': '347b85f18bd488493e87',
    'userId': '1133',
}

gameId = '3887'


class API:

    def getBoardString(gameID):
        url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=boardString&gameId=3724"

        payload = {}

        params = {
            'type': 'boardString',
            'gameId': gameID
        }

        response = requests.request(
            "GET", url, params=params, headers=headers, data=payload)

        return response.text

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
API.getBoardString(3724)
