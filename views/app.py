
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler


app = Flask('main1xx')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://us:pwd#@192.168.30.3/activiti_api'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 数据库
db = SQLAlchemy(app)
#定时任务
scheduler = APScheduler()



