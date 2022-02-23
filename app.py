from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
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

@app.route("/")
def hello_world():
    #login = Login(id=7, username="User7", email="abc7@gmail.com", password="incorrectpassword7")
    #db.session.add(login)
    #db.session.commit()
    return render_template('index.html')
    #return "<p>Hello, World!</p>"

@app.route("/registration")
def registration():
    return "This is the registration page"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
