from api import *
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


class TestUser:

    def test_user_get(self):
        """Test users list retrieval using GET command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        get = user.fetch()  # 200

    def test_user_create(self):
        """Test user creation using POST command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201

    def test_user_update(self):
        """Test user info update using PATCH command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        user.update()  # 200

    def test_user_upgrade(self):
        """Test user info upgrade using PUT command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        user.upgrade()

    def test_user_delete(self):
        """Test user deletion using DELETE command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        user.delete()

    def test_user_create_negative(self):
        """Test user creation negative response using POST command
        """
        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        try:
            user.create()
        except HTTPError:
            assert user.response.json()[0]['message'] == 'has already been taken', 'The message is not as expected'
            assert user.response.json()[0]['field'] == 'email', 'The message is not as excepted'


class TestPost:

    def test_post_get(self):
        """Test posts list retrieval using GET command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        get = post.fetch()  # 200

    def test_post_create(self):
        """Test post creation using POST command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201

    def test_post_update(self):
        """Test post info update using PATCH command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        post.update()  # 200

    def test_post_upgrade(self):
        """Test post info upgrade using PUT command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        post.upgrade()

    def test_post_delete(self):
        """Test post deletion using DELETE command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        post.delete()


class TestComment:

    def test_comment_get(self):
        """Test comments list retrieval using GET command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        comment = Comments(post_id=post.id, name=user.id, email=email, body=comment_body)
        get = comment.fetch()  # 200

    def test_comment_create(self):
        """Test comment creation using POST command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        comment = Comments(post_id=post.id, name=user.id, email=email, body=comment_body)
        comment.create()  # 201

    def test_comment_update(self):
        """Test comment info update using PATCH command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        comment = Comments(post_id=post.id, name=user.id, email=email, body=comment_body)
        comment.create()  # 201
        comment.update()  # 200

    def test_comment_upgrade(self):
        """Test comment info upgrade using PUT command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        comment = Comments(post_id=post.id, name=user.id, email=email, body=comment_body)
        comment.create()  # 201
        comment.upgrade()

    def test_comment_delete(self):
        """Test comment deletion using DELETE command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        comment = Comments(post_id=post.id, name=user.id, email=email, body=comment_body)
        comment.create()  # 201
        comment.delete()


class TestTodo:

    def test_todo_get(self):
        """Test todos list retrieval using GET command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        todo = Todos(user_id=user.id, title=todo_title, due_on=due_on, status=todo_status)
        todo = todo.fetch()  # 200

    def test_todo_create(self):
        """Test todos creation using POST command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        todo = Todos(user_id=user.id, title=todo_title, due_on=due_on, status=todo_status)
        todo.create()  # 201

    def test_todo_update(self):
        """Test todos info update using PATCH command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        todo = Todos(user_id=user.id, title=todo_title, due_on=due_on, status=todo_status)
        todo.create()  # 201
        todo.update()  # 200

    def test_todo_upgrade(self):
        """Test todos info upgrade using PUT command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        todo = Todos(user_id=user.id, title=todo_title, due_on=due_on, status=todo_status)
        todo.create()  # 201
        todo.upgrade()

    def test_todo_delete(self):
        """Test todos deletion using DELETE command
        """

        user = Users(name=name, email=email, gender=gender, status=user_status)
        user.create()  # 201
        post = Posts(user_id=user.id, title=post_title, body=post_body)
        post.create()  # 201
        todo = Todos(user_id=user.id, title=todo_title, due_on=due_on, status=todo_status)
        todo.create()  # 201
        todo.delete()
