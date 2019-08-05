from flask import Flask
from flask import request
import dataManager

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your brower is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s<h1>' % name

@app.route('/user/pws.json', methods = ['GET', 'POST'])
def password():
    if request.method == 'POST':
        words = request.form['pwd']

    elif request.method == 'GET':
        words = request.args.get('pwd')

    if words:
        return '<h1>转换后的timestamp是: %s<h1>' % dataManager.datestamp(words)

if __name__== '__main__':
    print('start') # main函数中添加代码, 在启动flask的时候, 这些代码就会首先运行.
    app.run(host='10.15.5.164', port='8989')
