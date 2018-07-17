
import random
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for)

bp = Blueprint('quiz', __name__)



@bp.route('/quiz', methods=('GET', 'POST'))
def quiz():
    return render_template('radioquiz/radioquiz.html')



@bp.route('/rwalk', methods=('GET', 'POST'))
def rwalk():
    the_range = []
    for i in range(25):
        the_range.append(random.randrange(0, 25))

    return render_template('radioquiz/rwalk.html', the_range=the_range)
