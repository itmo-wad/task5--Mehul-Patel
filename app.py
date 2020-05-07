from flask import Flask, send_from_directory, render_template
from flask import request, redirect, flash

app = Flask(__name__)

app.secret_key = 'key'
db = {'admin': '123456'}

@app.route('/', methods=['GET', 'POST'])
def login_user():
    global s
    try:
        if db[request.form['user']] == request.form['pwd']:
            s = True
            return redirect('cabinet')
    except:
        msg = "not post request"
    return render_template('login.html')

@app.route('/cabinet')
def cabinet():
    if s == True:
        return render_template('index.html')
    else:
        return redirect('/')

@app.route('/img/<path:filename>')
def imgFile(filename):
    return send_from_directory('/static/img', filename)

@app.route('/static/css/<string:stylesheet>')
def css(stylesheet):
    return send_from_directory('static/css', stylesheet)

if __name__ == "__main__":
    app.run(debug=True)
