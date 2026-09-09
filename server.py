from flask import Flask, render_template, redirect, request

app = Flask(__name__)
data = [
    ['admin', '05519218']
]


def ai (q):
    if q:
        return 'سلام من یک هوش مصتوعی هستم و هنوز آماده برای کمک به شما نشده ام !\nHello, I am an AI, and I am not yet ready to help you!'

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/login', methods=["get"])
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['post'])
def login():
    name = request.form['username']
    password = request.form['password']
    for i in data:
        if name == i[0] and password == i[1]:
            return redirect('/page')
        elif name == '' and password == '':
            return '<h1>please enter something !</h1>'
    else:
        return render_template('bad_login.html')

@app.route('/page', methods=['GET', 'POST'])
def page():
    answer = ''
    if request.method == 'POST':
        message = request.form['message']
        answer = ai(message)
    return render_template('page.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

