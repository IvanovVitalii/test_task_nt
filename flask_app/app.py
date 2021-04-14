from flask import Flask, request
from flask_app.functions import *

app = Flask(__name__)


@app.route('/start', methods=['GET'])
def json_example():
    try:
        req = request.get_json()
        data = req['data']
        rules = req['rule']
    except TypeError as e:
        return f'{e}'
    result = []
    for number in data:
        calculations = 0
        for rule in rules:
            calculations += methods[rule](int(number))
        result.append(calculations)
    return '{result: ' + f'{result}' + '}'


if __name__ == '__main__':
    app.run(debug=True)
