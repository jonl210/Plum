from flask import Blueprint, render_template

from peewee import *

from .shortener import MiniLink

#Blueprint
bp = Blueprint('link', __name__, url_prefix='/link')

#Display info for shortened link
@bp.route('/id/<u_id>')
def link_view(u_id):
    link = MiniLink.get(u_id=u_id)
    return render_template('link.html', link=link)
