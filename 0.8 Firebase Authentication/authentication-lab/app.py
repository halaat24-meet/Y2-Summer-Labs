from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config={
    "apiKey": "AIzaSyC2MtYElQPx9k05stxcwCf6Ex3XAk6Xh18",
    "authDomain": "authentication-81c17.firebaseapp.com",
    "projectId": "authentication-81c17",
    "storageBucket": "authentication-81c17.appspot.com",
    "messagingSenderId": "687020370548",
    "appId": "1:687020370548:web:cefd5dcdac2fd18d1bbf21",
    "measurementId": "G-WP2CGR3024",
    "databaseURL": ""

  }
  
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)