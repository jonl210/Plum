from flask import Blueprint, flash, redirect, render_template, request, url_for

#Blueprint
bp = Blueprint('shortener', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
