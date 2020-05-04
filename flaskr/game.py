from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
        )

from flaskr.model import *

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/running', methods=['GET'])
def running():
    state = get_state()
    if state == False:
        return redirect(url_for('.start'))
    return render_template('game/running.html',state=state, rows=len(state),columns=len(state[0]))

@bp.route('/state_change')
def state_change():
    row = int(request.args.get('row'))
    column = int(request.args.get('column'))
    if row != None and column != None:
        if not(update_state(row,column)):
            error = "Failed to update game state"         
            flash(error)
    return redirect(url_for('.running'))


@bp.route('/running_state', methods=['GET'])
def running_state():
    row = request.args.get('row')
    column = request.args.get('column')
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
    if rows==None or columns==None:
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
    else:
        if create_state(int(rows), int(columns)):
            return redirect(url_for('game.running'))
        else:
            error = "Failed to start game"
            flash(error)
            
            return render_template('game/start.html')    


