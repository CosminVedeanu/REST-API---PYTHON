import requests

#GET
class Fetch:

    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = {'Authorization': api_key}

    def request(self):
        response = requests.get(self.api_url, headers=self.api_key)
        return response