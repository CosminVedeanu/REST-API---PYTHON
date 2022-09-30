import requests

#GET
class Todos:

    def __init__(self, api_url, api_key, id, payload):
        self.api_url = api_url
        self.api_key = {'Authorization': api_key}
        self.api_url_id = f'{api_url}/{id}'
        self.payload = payload

    # GET
    def fetch(self):
        get = requests.get(self.api_url, headers=self.api_key)
        print('GET', get.json(), get.status_code, sep='\n')
        return get

    # POST
    def create(self):
        post = requests.post(self.api_url, json=self.payload, headers=self.api_key)
        print('POST', post.json(), post.status_code, sep='\n')
        return post

    # PATCH
    def update(self):
        patch = requests.patch(self.api_url_id, json=self.payload, headers=self.api_key)
        print('PATCH', patch.json(), patch.status_code, sep='\n')
        return patch

    # PUT
    def upgrade(self):
        put = requests.put(self.api_url_id, json=self.payload, headers=self.api_key)
        print('PUT', put.json(), put.status_code, sep='\n')
        return put

    # DELETE
    def delete(self):
        delete = requests.delete(self.api_url_id, headers=self.api_key)
        print('DELETE', delete.status_code, sep='\n')
        return delete

    # PAYLOAD
    def set_payload(self, payload):
        self.payload = payload