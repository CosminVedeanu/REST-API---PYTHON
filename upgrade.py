import requests

#PUT
class Upgrade:

    def __init__(self, api_url, api_key, put):
        self.api_url = api_url
        self.api_key = {'Authorization': api_key}
        self.put = put
    def request(self):
        response = requests.put(self.api_url, json=self.put , headers=self.api_key)
        return response