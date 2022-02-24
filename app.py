from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from jinja2 import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userinformation.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20),unique=True , nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self) -> (int,str):
        return f"{self.id} - {self.username}"

class userInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self) -> (int,str):
        return f"{self.id} - {self.firstname}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        print(id), print(firstname), print(lastname), print(address),print(city), print(state), print(zip)
        userinfo = userInfo(id=id, firstname=firstname, lastname=lastname, address=address, city=city, state=state, zip=zip)
        db.session.add(userinfo)
        db.session.commit()
#        id = request.form['id']
 #       username = request.form['username']
  #      email = request.form['email']
   #     password = request.form['password']
    #    print(id),print(username),print(email),print(password)
     #   login = Login(id=id, username=username, email=email, password=password)
      #  db.session.add(login)
       # db.session.commit()
    return render_template('index.html')

@app.route("/registration")
def registration():
    return "This is the registration page"

@app.route("/table")
def show():
#    alllogin = Login.query.all()
    userinfo = userInfo.query.all()
    return render_template('table.html', userinfo=userinfo)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
