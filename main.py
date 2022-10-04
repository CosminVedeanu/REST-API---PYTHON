from API import Users, Posts, Comments, Todos

#users
user_id = '6180'
name = 'Cosmin21'
email = 'Cosmin@45215.com'
gender = 'male'
user_status = 'active'

#posts
post_title = 'Carbunele1'
post_body = 'Carbunele este o roca sedimentara1'

#comments
comment_body = 'Foarte informativ1'

#todos
todo_title = 'Carbunele1'
due_on = '2022-10-18T00:00:00.000+05:30'
todo_status = 'pending'


users = Users(user_id)
get = users.fetch() #200
users.set_payload(name, email, gender, user_status)
user_id = users.create() #201
users.set_payload(name, email, gender, user_status)
users.upgrade() #200
users.update() #200
#users.delete() #204

posts = Posts(user_id)
get = posts.fetch() #200
posts.set_payload(user_id, post_title, post_body)
post_id = posts.create() #201
posts.set_payload(user_id, post_title, post_body)
posts.upgrade() #200
posts.update() #200
#posts.delete() #204

comments = Comments(post_id)
get = comments.fetch() #200
comments.set_payload(post_id, user_id, email, comment_body)
comment_id = comments.create() #201
comments.set_payload(post_id, user_id, email, comment_body)
comments.upgrade() #200
comments.update() #200
#comments.delete() #204

todos = Todos(user_id)
get = todos.fetch() #200
todos.set_payload(user_id, todo_title, due_on, todo_status)
todo_id = todos.create() #201
todos.set_payload(user_id, todo_title, due_on, todo_status)
todos.upgrade() #200
todos.update() #200
#todos.delete() #204
