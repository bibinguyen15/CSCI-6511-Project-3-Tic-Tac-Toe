import requests


url = 'https://www.notexponential.com/aip2pgaming/api/index.php'


class API:

    def getBoard():
        url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=boardString&gameId=3724"
        headers = {
            'x-api-key': '347b85f18bd488493e87',
            'userId': '1133'
        }
        payload = {}
        params = {
            'type': 'boardString',
            'gameId': '3724'
        }

        response = requests.request("GET", url, headers=headers,
                                    params=params, data=payload)

        if response.status_code == 200:
            print(response.text)
        else:
            print(f'Request failed with status code {response.status_code}')


API.getBoard()
