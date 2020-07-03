import os

SECRET_KEY = 'p9Bv<3Eid9%$i01'

# """ Use pymysql instead MySQLdb, because MySQLdb is not supported by Python3 """
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://local_admin:12345678@localhost/local_db'

HOST = "http://localhost:8081/"

RABBITMQ_PORT = os.environ.get("RABBITMQ_PORT")
RABBITMQ_DEFAULT_USER = os.environ.get("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.environ.get("RABBITMQ_DEFAULT_PASS")
RABBITMQ_DEFAULT_VHOST = os.environ.get("RABBITMQ_DEFAULT_VHOST")
RABBITMQ_DEFAULT_HOST = os.environ.get("RABBITMQ_DEFAULT_HOST")

WORKER_TOKEN = os.environ.get("WORKER_TOKEN")
