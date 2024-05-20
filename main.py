from flask import  Flask,flash,redirect,render_template
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'igorkeven'


@app.route("/")
def home():
    return render_template("home.html")





if __name__ in '__main__':
    app.run()