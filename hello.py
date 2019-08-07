from flask import Flask, jsonify
from flask import request
import dataManager
import model
import json

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>{}, Your brower is {}</p>'.format(globle_variable, user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s<h1>' % name

@app.route('/user/pws.json', methods = ['GET', 'POST'])
def password():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        words = data['pwd']
        # words = request.form['pwd']

    elif request.method == 'GET':
        words = request.args.get('pwd')

    if words:
        # return '<h1>转换后的timestamp是: %s<h1>' % dataManager.datestamp(words)
        return '<h1>转换后的timestamp是: %s<h1>' % words

@app.route('/login', methods = ['POST'])
def login():
    print(request.get_data())
    # data = json.loads(request.get_data())
    # print(request.form['username'])
    username = request.form["username"]
    password = request.form["password"]
    return jsonify({"login": username, "psw":password}) # 返回布尔值

@app.route('/xgb')
def runxgb():
    return '<h1>MSE:{} in XGBR<h1>'.format(model.xgb_test())

if __name__== '__main__':
    print('Flask Start') # main函数中添加代码, 在启动flask的时候, 这些代码就会首先运行.
    globle_variable = 'Hello Flask'
    app.run(host='0.0.0.0', port='8989')
