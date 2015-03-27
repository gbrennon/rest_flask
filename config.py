class BaseConfig(object):
    DEBUG = True


class TestConfig(BaseConfig):
    TESTING = True
    MONGODB_SETTINGS = {'db': 'pycangaco_test'}


class DevConfig(BaseConfig):
    TESTING = False
    MONGODB_SETTINGS = {'db': 'pycangaco_dev'}
