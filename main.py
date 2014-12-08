from flask import Flask
from locationNinja.models import Event
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///location-ninja.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/event/')
def event():
    temp = Event.Event("Alpha 1", "Rondebosch")
    return str(temp)

@app.route('/user/')
def user():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


