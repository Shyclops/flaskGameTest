from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
        )

from flaskr.model import *

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/running', methods=['GET', 'POST'])
def running(row=None, column=None):
    if request.method=='POST':
        if row == None or column == None:
            row = request.form['row']
            column  = request.form['column']
        if row != None and column != None:
            if not(update_state(int(row),int(column))):
                error = "Failed to update game state"
                flash(error)
    state = get_state()
    if state == False:
        return redirect(url_for('.start'))
    return render_template('game/running.html',state=state, rows=len(state),columns=len(state[0]))

@bp.route('/running_state', methods=['GET', 'POST'])
def running_state(row=None, column=None):
    if request.method == 'POST':
        game_state = get_state()
        if row==None or column==None:
            try:
                return jsonify(game_state)
            except:
                return jsonify(False)
        else:
            try:
                state = game_state[int(row)][int(column)]
                return jsonify(state)
            except:
                return jsonify(False)


@bp.route('/start', methods=['GET', 'POST'])
def start(rows=None, columns=None):
    if request.method == 'POST':
        rows = request.form['rows']
        columns  = request.form['columns']
        error = None
        try:
            rows = int(rows)
            columns = int(columns)
        except ValueError:
            error = "Please input integers"

        if rows < 1 or columns < 1:
            error = "Please specify a positive dimension"

        if error is None:
            if create_state(rows, columns):
                return redirect(url_for('game.running'))
            else:
                error = "Failed to start game"

        flash(error)

    return render_template('game/start.html')


