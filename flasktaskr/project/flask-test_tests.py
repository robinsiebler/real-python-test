# example of how to use Flask-Testing (not supported by PyCharm)


import os
import unittest
import flask.ext.testing
from flask import Flask
from flask.ext.testing import TestCase


from views import app, db
from _config import basedir
from models import User

TEST_DB = 'test.db'


class AllTests(TestCase):

	render_templates = False
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, TEST_DB)

	def create_app(self):
		return app

	def setup(self):
		db.create_all()


	# executed after each test
	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_user_setup(self):
		new_user = User("michael", "michael@mherman.org", "michaelherman")
		db.session.add(new_user)
		db.session.commit()
		assert new_user in db.session


if __name__ == "__main__":
	unittest.main()
