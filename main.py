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

user = Users(name, email, gender, user_status)
get = user.fetch() #200
user.create() #201
user.upgrade() #200
user.update() #200
#users.delete() #204

post = Posts(user.id, post_title, post_body)
get = post.fetch() #200
post.create() #201
post.upgrade() #200
post.update() #200
#posts.delete() #204

comment = Comments(post.id, user.id, email, comment_body)
get = comment.fetch() #200
comment.create() #201
comment.upgrade() #200
comment.update() #200
#comments.delete() #204

todo = Todos(user.id, todo_title, due_on, todo_status)
get = todo.fetch() #200
todo.create() #201
todo.upgrade() #200
todo.update() #200
#todos.delete() #204

clean = Api(1)
clean.cleanup()