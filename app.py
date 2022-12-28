from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/cataloge')
def cataloge():
    return render_template("cataloge.html")



@app.route('/cataloge2')
def cataloge2():
    return render_template("cataloge2.html")


@app.route('/cataloge3')
def cataloge3():
    return render_template("cataloge3.html")



@app.route('/cataloge4')
def cataloge4():
    return render_template("cataloge4.html")


@app.route('/cataloge5')
def cataloge5():
    return render_template("cataloge5.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html")


@app.route('/login')
def login():
    return render_template("login.html")



if __name__ == "__main__":
    app.run()
