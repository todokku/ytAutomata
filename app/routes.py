from app import app
from flask import jsonify, request, abort
from flask_cors import CORS, cross_origin
from app.automata.model import Automata
from selenium import webdriver

cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})


@app.route('/automata', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def automata():
    if not request.json:
        return abort(500)
    accounts = request.json.get('accounts')
    channelURL = request.json.get('channelURL')
    driver = webdriver.Chrome()
    response = []

    for account in accounts:
        automata = Automata(account, channelURL, driver)
        response.append(automata.execute())

    driver.quit()
    return jsonify({
        'status': 200,
        'response': response
    })
