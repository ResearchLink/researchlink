# coding=utf-8
from services.app import DebugConfig, init_app, gevent_run
import os

basedir = os.path.dirname(os.path.abspath(__file__)) or "."


class MyConfig(DebugConfig):
    # override default Configs
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    LOGGING_FILE = os.path.join(basedir, "logs", "app.log")
    UPLOAD_DIR = os.path.join(basedir, "uploads")


class ProductionConfig(DebugConfig):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://researchlink:researchlink@127.0.0.1:3306/researchlink'
    LOGGING_FILE = os.path.join(basedir, "logs", "app.log")
    UPLOAD_FOLDER = os.path.join(basedir, "uploads")


app = init_app(ProductionConfig)

if __name__ == "__main__":
    # for debug only
    gevent_run(app, "0.0.0.0", 5000)
