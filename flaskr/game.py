from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
        )

import flaskr.model

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/running', methods=['GET'])
def running():
    state = model.get_state()
    return render_template('game/running.html',state)

@bp.route('/running_state/<int:row>_<int:column>', methods=['GET', 'POST'])
def running_state(row=None, column=None):
    if request.method == 'GET':
        game_state = model.get_state()
        if row==None or column==None:
            return jsonify(game_state)
        else:
            state = game_state[row][column]
            return jsonify(state)
    else:
        return jsonify(model.update_state(row,column))


@bp.route('/start', methods=['GET', 'POST'])
def start():
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
            if model.create_state(rows, columns):
                return redirect(url_for('game.running'))
            else:
                error = "Failed to start game"

        flash(error)

    return render_template('game/start.html')


