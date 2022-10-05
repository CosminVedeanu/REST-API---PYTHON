import requests
from auth import api_key, api_url

#GET
class API:
    def __init__(self, id):
        self.api_key = api_key
        self.api_url = f'{api_url}users'
        self.id = id
    # GET
    def fetch(self):
        response = requests.get(self.api_url, headers=self.api_key)
        print('GET', response.json(), response.status_code, sep='\n')
        return response

    # POST
    def create(self):
        response = requests.post(self.api_url, json=self.payload, headers=self.api_key)
        print('POST', response.json(), response.status_code, sep='\n')
        try:
            self.id = response.json()['id']
            return self.id
        except TypeError:
            print("Id already in use")
    # PATCH
    def update(self):
        response = requests.patch(self.api_url_id, json=self.payload, headers=self.api_key)
        print('PATCH', response.json(), response.status_code, sep='\n')

    # PUT
    def upgrade(self):
        response = requests.put(self.api_url_id, json=self.payload, headers=self.api_key)
        print('PUT', response.json(), response.status_code, sep='\n')

    # DELETE
    def delete(self):
        response = requests.delete(self.api_url_id, headers=self.api_key)
        print('DELETE', response.status_code, sep='\n')

    # PAYLOAD
class Users(API):
    def set_payload(self, name, email, gender, status):
        self.payload = {"name": name, "email": email, "gender": gender, "status": status}
        self.api_url_id = f'{self.api_url}/{self.id}'

class Posts(API):
    def set_payload(self, user_id, title, body):
        self.payload = {"user_id": user_id, "title": title, "body": body}
        self.api_url_id = f'{self.api_url}/{self.id}'

class Comments(API):
    def set_payload(self, post_id, name, email, body):
        self.payload = {"post_id": post_id, "name": name, "email": email, "body": body}
        self.api_url_id = f'{self.api_url}/{self.id}'

class Todos(API):
    def set_payload(self, user_id, title, due_on, status):
        self.payload = {"user_id": user_id, "title": title, "due_on": due_on, "status": status}
        self.api_url_id = f'{self.api_url}/{self.id}'
