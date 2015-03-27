from flask.ext.testing import TestCase
from api import create_app as create_app_base


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app_base('config.TestConfig')
