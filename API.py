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


class API:

    def get_board_string():
        url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=boardString&gameId=3724"

        payload = {}

        params = {
            'type': 'boardString',
            'gameId': '3724'
        }

        response = requests.request(
            "GET", url, params=params, headers=headers, data=payload)

        print(response.text)


API.get_board_string()
