from flask import Blueprint, redirect, render_template, request, url_for

from peewee import *

import random, string

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
    visit_count = IntegerField(default=0)

#Run to add tables to database
# mysql_db.connect()
# mysql_db.create_tables([MiniLink])

#Main page
@bp.route('/', methods=('GET', 'POST'))
def index():
    #If post, create mini link
    if request.method == "POST":
        url = request.form["url"]
        u_id = generate_unique_id()
        mini_url = url_for('.shortened_link', u_id=u_id, _external=True)
        MiniLink.create(original_url=url, mini_url=mini_url, u_id=u_id)
        return redirect(url_for('index'))

    link_count = MiniLink.select().count()
    return render_template('index.html', link_count=link_count)

#Redirect to original url from mini link
@bp.route('/<u_id>')
def shortened_link(u_id):
    link = MiniLink.get(u_id=u_id)
    link.visit_count += 1
    link.save()
    return redirect(link.original_url)

#Generate unique id for mini link
def generate_unique_id():
    unique = False
    random_id = 0

    #Check if id already exists
    while not unique:
        random_id = ''.join([random.choice(string.ascii_letters +
            string.digits) for n in range(8)])

        if MiniLink.get_or_none(MiniLink.u_id == random_id) != None:
            unique = False
        else:
            unique = True

    return random_id
