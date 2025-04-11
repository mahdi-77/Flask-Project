from flask import Flask, render_template, request ,   g, redirect,render_template, request, session, url_for

import pickle
import numpy as np


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='khalil', password='1234'))
users.append(User(id=2, username='ahmed', password='9999'))
users.append(User(id=3, username='ghassen', password='5896'))


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('index.html')





# hna tamel chargement mtta l modele
model = pickle.load(open('iri.pkl', 'rb'))













@app.route('/predict', methods=['POST'])
def home():
  
    data5 = request.form['e']
    arr = np.array([[1, 1, 1, 1]])
    pred = model.predict(arr)
    return render_template('pred.html', data=pred ,data2=data5)


if __name__ == "__main__":
    app.run(debug=True)















