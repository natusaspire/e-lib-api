import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

SECRET_KEY = 'cbb1828c78810f336f6bdf5791d62e9c'
