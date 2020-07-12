from flask import Flask, jsonify, request, render_template
from flask_cors import CORS


app=Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET', 'POST'])
@cross_origin()
def hello():

    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())
        return 'OK', 200

    else:
        message = {'greeting':'Hello from Flask'}
        return jsonify(message)

@app.route('/test')
def test_page():
    return render_template('index.html')  

