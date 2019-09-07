from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World aaddd sss dddd'

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f"Sorry -- {name} you are not old enough"), 401

@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    return jsonify(message=f"Sorry ** {name} you are not old enough {age}"), 401

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)