from api import Api, Users, Posts, Comments, Todos
import random

#users
name = f'Cosmin{random.random()}'
email = f'Cosmin@{random.random()}.com'
gender = 'male'
user_status = 'active'

#posts
post_title = f'Carbunele{random.random()}'
post_body = f'Carbunele este o roca sedimentara.{random.random()}'

#comments
comment_body = f'Foarte informativ.{random.random()}'

#todos
todo_title = f'Carbunele{random.random()}'
due_on = '2022-10-18T00:00:00.000+05:30'
todo_status = 'pending'

users = Users(name, email, gender, user_status)
get = users.fetch() #200
users.set_payload()
user_id = users.create() #201
users.set_payload()
users.upgrade() #200
users.update() #200
#users.delete() #204

posts = Posts(user_id, post_title, post_body)
get = posts.fetch() #200
posts.set_payload()
post_id = posts.create() #201
posts.set_payload()
posts.upgrade() #200
posts.update() #200
#posts.delete() #204

comments = Comments(post_id, user_id, email, comment_body)
get = comments.fetch() #200
comments.set_payload()
comment_id = comments.create() #201
comments.set_payload()
comments.upgrade() #200
comments.update() #200
#comments.delete() #204

todos = Todos(user_id, todo_title, due_on, todo_status)
get = todos.fetch() #200
todos.set_payload()
todo_id = todos.create() #201
todos.set_payload()
todos.upgrade() #200
todos.update() #200
#todos.delete() #204

clean = Api(1)
clean.cleanup()