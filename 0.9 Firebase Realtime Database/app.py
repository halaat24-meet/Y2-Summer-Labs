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
    "databaseURL": "https://authentication-81c17-default-rtdb.europe-west1.firebasedatabase.app/"

  }


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        full_name= request.form['full_name']
        username=request.form['username']
        user={"full_name":full_name, "email":email, "username":username}
        try: 
            session['user']=auth.create_user_with_email_and_password(email, password)
            session['quotes']=[]
            uid=session['user']['localId']
            session.modified = True 
            db.child("users").child(uid).set(user)
            return render_template("home.html")
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
        text = request.form['quote']
        person= request.form['person']
        uid=session['user']['localId']
        quote={"text":text, "said_by":person, "uid":uid}
        db.child("Quotes").push(quote)

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
   quotes_d=db.child("Quotes").get().val()
   return  render_template("display.html", quotes=quotes_d)

if __name__ == '__main__':
    app.run(debug=True)