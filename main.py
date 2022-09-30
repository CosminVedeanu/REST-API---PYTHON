from users import Users
from posts import Posts
from comments import Comments
from todos import Todos


api_key = 'Bearer e79dddf3177e7d2c5c86baa5bb491bae32f350b1822957a12fdd0d819743400e'
id = '3723'

#users
api_url = 'https://gorest.co.in/public/v2/users'
payload = {"name": "Carbunele", "email": "Carbunele@carbunele.com", "gender": "male", "status": "active"}

users = Users(api_url, api_key, id, payload)

get = users.fetch() #200
post = users.create() #201
users.set_payload({"id": id, "name": "Cartoful", "email": "Cartoful@cartof.com", "gender": "male", "status": "active"})
put = users.upgrade() #200
users.set_payload({"id": id, "gender": "female"})
patch = users.update() #200
#delete = users.delete() #204

#posts
api_url = 'https://gorest.co.in/public/v2/posts'
payload = {"user_id": id,"title": "Carbunele.","body": "Carbunele este o roca sedimentara"}

posts = Posts(api_url, api_key, id, payload)

get = posts.fetch() #200
post = posts.create() #201
posts.set_payload({"id": id, "user_id": id,"title": "Carbunele.","body": "Carbunele este o roca."})
put = posts.upgrade() #200
posts.set_payload({"id": id, "body": "Frumos"})
patch = posts.update() #200
delete = posts.delete() #204

#comments
api_url = 'https://gorest.co.in/public/v2/comments'
payload = {"id": id, "post_id": 1558, "name": "Cartoful", "email": "Cartoful@cartof.com", "body": "Foarte informativ"}

comments = Comments(api_url, api_key, id, payload)

get = comments.fetch() #200
post = comments.create() #201
comments.set_payload({"id": id, "post_id": 1558, "name": "Cartoful", "email": "Cartoful@cartof.com", "body": "Perfect"})
put = comments.upgrade() #200
users.set_payload({"id": id, "body": "Adevarat"})
patch = comments.update() #200
delete = comments.delete() #204

#todos
api_url = 'https://gorest.co.in/public/v2/todos'
payload = {"id": 1597,"user_id": id,"title": "Carbunele","due_on": "2022-10-18T00:00:00.000+05:30","status": "pending"}

todos = Todos(api_url, api_key, id, payload)

get = todos.fetch() #200
post = todos.create() #201
todos.set_payload({"id": 1597,"user_id": id,"title": "Cartoful","status": "completed"})
put = todos.upgrade() #200
todos.set_payload({"id": id, "status": "pending"})
patch = todos.update() #200
delete = todos.delete() #204