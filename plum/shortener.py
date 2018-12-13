from flask import Blueprint, flash, redirect, render_template, request, url_for

from peewee import *

#Blueprint
bp = Blueprint('shortener', __name__)

#Database info
mysql_db = MySQLDatabase('plumdb', user='root', password='dentyne40',
                    host='localhost', port=3316)

class BaseModel(Model): #Base model
    class Meta:
        database = mysql_db

class MiniLink(BaseModel): #Shortened link model
    original_url = TextField()
    mini_url = TextField()
    u_id = CharField(max_length=8)

#Run to add tables to database
# mysql_db.connect()
# mysql_db.create_tables([MiniLink])

@bp.route('/')
def index():
    return render_template('index.html')
