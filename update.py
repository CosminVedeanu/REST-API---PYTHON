import requests

#PATCH
class Update:

    def __init__(self, api_url, api_key, patch):
        self.api_url = api_url
        self.api_key = {'Authorization': api_key}
        self.patch = patch
    def request(self):
        response = requests.patch(self.api_url, json=self.patch, headers=self.api_key)
        return response