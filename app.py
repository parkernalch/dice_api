import flask
import random
from dieroll import roll, evaluate
from flask import request, jsonify
from flask_cors import CORS


app  = flask.Flask(__name__)
app.config['DEBUG'] = False
cors = CORS(app)

@app.route('/', methods=['GET'])
def home():
    return flask.render_template('layout.html')

@app.route('/roll', methods=['GET', 'POST'])
def roll():
    if request.method == 'GET':
        rollequation = ''
        if 'eq' in request.args:
            rollequation = str(request.args['eq'])

        # print(rollequation)
        res = evaluate(rollequation)
        return jsonify(res)
        # return jsonify(Roll(rollequation))
        # return str(random.randint(1, 20))
    
    req = request.get_json()
    rollequation = req['equation']
    # return jsonify(Roll(rollequation))
    res = evaluate(rollequation)

    # res = flask.make_response()
    # res['result'] = evaluate(rollequation)
    
    # if str(res)[:1] == "U":
    #     res['status'] = 400
    #     res['err'] = "Unimplemented error"
    #     res['xhr'] = ""

    return jsonify(res)

# app.run()
