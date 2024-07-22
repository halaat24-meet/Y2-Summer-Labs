from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
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
def signup():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        try: 
            session['user']=auth.create_user_with_email_and_password(email, password)
            session['quotes']=[]
            session.modified = True 
        except:
            error="authentication failed!!"
            print(error)
        return redirect(url_for("home"))

    else:
        return render_template("signup.html")




@app.route('/signin', methods=['GET', 'POST'])
def signin():
        if request.method=='POST':
            email = request.form['email']
            password = request.form['password']
            try: 
                session['user']=auth.create_user_with_email_and_password(email, password)
                session['quotes']=[]
                session.modified = True
            except:
                error="authentication failed!!"
                print(error)
            return redirect(url_for("home"))
        else:
            return render_template("signin.html")



@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        message=request.form['Name']
        session['quotes'].append(message)
        session.modified = True
        return redirect((url_for('thanks')))
    else:
        return render_template("home.html")


@app.route('/signout', methods=['GET', 'POST'])
def signout():
    session['user']=None
    auth.current_user = None
    print("the user is signed out")
    return redirect((url_for('signin')))



@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template("thanks.html")



@app.route('/display', methods=['GET', 'POST'])
def display():
    YES= session['quotes']
    print(YES)
    return render_template(
        'display.html', n = YES)


if __name__ == '__main__':
    app.run(debug=True)