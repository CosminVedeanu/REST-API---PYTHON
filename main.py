from fetch import Fetch
from create import Create
from upgrade import Upgrade
from update import Update
from delete import Delete

api_key = 'Bearer e79dddf3177e7d2c5c86baa5bb491bae32f350b1822957a12fdd0d819743400e'

#USERS
user = '/3889'
api_url = 'https://gorest.co.in/public/v2/users'
api_url_user = f'{api_url}{user}'
post = {"name": "Carbunele", "email": "Carbunele@carbunele.com", "gender": "male", "status": "active"}
put = {"id": 3869, "name": "Carbunele69", "email": "Carbunele69@carbunele.com", "gender": "male", "status": "active"}
patch ={"id": 3869, "gender": "female"}

users_fetch = Fetch(api_url, api_key)
users_get = users_fetch.request()

users_upgrade = Upgrade(api_url_user, api_key, put)
users_put = users_upgrade.request()

users_update = Update(api_url_user, api_key, patch)
users_patch = users_update.request()

users_d = Delete(api_url_user, api_key)
users_delete = users_d.request()

users_create = Create(api_url, api_key, post)
users_post = users_create.request()

print("GET")
print(users_get.json())
print(users_get.status_code) #200

print("PUT")
print(users_put.json())
print(users_put.status_code) #200

print("PATCH")
print(users_patch.json())
print(users_patch.status_code) #200

print("DELETE")
print(users_delete.status_code) #204

print("POST")
print(users_post.json())
print(users_post.status_code) #201

