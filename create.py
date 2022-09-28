import requests

#POST
class Create:

    def __init__(self, api_url, api_key, post):
        self.api_url = api_url
        self.api_key = {'Authorization': api_key}
        self.post = post

    def request(self):
        response = requests.post(self.api_url ,json=self.post, headers=self.api_key)
        return response