

from flask import Flask, render_template, url_for, redirect, request
import random

app = Flask(__name__, template_folder="templates")

@app.route('/create', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home2.html')
    else:
        Birth_month = request.form['Birth_month']
        return redirect(url_for('response', b=Birth_month))

@app.route('/response/<b>')
def response(b):
    Fortunes = ["Many people eat cereal for breakfast, like you","You will go to the gym three times a week.","Your mother is becoming a teacher.","Your life is getting better","Don't give up","All our dreams can come true, if we have the courage to pursue them.","Spread love everywhere you go.","Everything you've ever wanted is sitting on the other side of fear.","The biggest risk is not taking any risk","there are grounds for hope"]

    birthmonthlenght=len(b)
    if birthmonthlenght>10:
        random_fortune=Fortunes[9]
    else:
        random_fortune=Fortunes[birthmonthlenght]
    return render_template('response.html', fortune=random_fortune,birth_month=b)

@app.route('/fortune')
def fortune():
    Fortunes = [
        "Many people eat cereal for breakfast, like you",
        "You will go to the gym three times a week.",
        "Your mother is becoming a teacher.",
        "Your life is getting better",
        "Don't give up",
        "All our dreams can come true, if we have the courage to pursue them.",
        "Spread love everywhere you go.",
        "Everything you've ever wanted is sitting on the other side of fear.",
        "The biggest risk is not taking any risk",
        "there are grounds for hope"
        ]

    birthmonthlenght=len(Birth_month)
    if birthmonthlenght>10:
        random_fortune=Fortunes[9]
    else:
        random_fortune=Fortunes[birthmonthlenght]

    return render_template('fortune.html', fortune=random_fortune)

if __name__ == '__main__':
    app.run(debug=True)