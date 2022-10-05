import requests
from auth import api_key, base_url

class Api:
    junk = []
    def __init__(self, id):
        self.api_key = api_key
        self.id = id
        self.response = {}
    # GET
    def fetch(self):
        response = requests.get(self.API_URL, headers=self.api_key)
        print('GET', response.json(), response.status_code, sep='\n')
        self.response = response
        return response

    # POST
    def create(self):
        response = requests.post(self.API_URL, json=self.payload, headers=self.api_key)
        print('POST', response.json(), response.status_code, sep='\n')
        self.id = response.json()['id']
        self.api_url_id = f'{self.API_URL}/{self.id}'
        self.response = response
        self.junk.append(self.api_url_id)
        return self.id

    # PATCH
    def update(self):
        response = requests.patch(self.api_url_id, json=self.payload, headers=self.api_key)
        print('PATCH', response.json(), response.status_code, sep='\n')
        self.response = response

    # PUT
    def upgrade(self):
        response = requests.put(self.api_url_id, json=self.payload, headers=self.api_key)
        print('PUT', response.json(), response.status_code, sep='\n')
        self.response = response

    # DELETE
    def delete(self):
        response = requests.delete(self.api_url_id, headers=self.api_key)
        print('DELETE', response.status_code, sep='\n')
        self.response = response

    def cleanup(self):
        for i in range(0, len(self.junk)):
            response = requests.delete(self.junk[i], headers=self.api_key)
            print(f'ID:{self.junk[i]} removed!', response.status_code, sep='\n')

    # PAYLOAD
class Users(Api):
    API_URL = f'{base_url}users'

    def __init__(self, name, email, gender, status, id=''):

        self.name = name
        self.email = email
        self.gender = gender
        self.status = status
        super().__init__(id)

    def set_payload(self):

        self.payload = {
            "name": self.name,
            "email": self.email,
            "gender": self.gender,
            "status": self.status
        }

class Posts(Api):
    API_URL = f'{base_url}posts'

    def __init__(self, user_id, title, body, id=''):
        self.user_id = user_id
        self.title = title
        self.body = body
        super().__init__(id)

    def set_payload(self):

        self.payload = {
            "user_id": self.user_id,
            "title": self.title,
            "body": self.body
        }

class Comments(Api):
    API_URL = f'{base_url}comments'

    def __init__(self, post_id, name, email, body, id=''):
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body
        super().__init__(id)

    def set_payload(self):

        self.payload = {
            "post_id": self.post_id,
            "name": self.name,
            "email": self.email,
            "body": self.body
        }

class Todos(Api):
    API_URL = f'{base_url}todos'

    def __init__(self, user_id, title, due_on, status, id=''):
        self.user_id = user_id
        self.title = title
        self.due_on = due_on
        self.status = status
        super().__init__(id)


    def set_payload(self):

        self.payload = {
            "user_id": self.user_id,
            "title": self.title,
            "due_on": self.due_on,
            "status": self.status
        }