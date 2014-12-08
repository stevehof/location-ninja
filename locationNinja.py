import vendor
vendor.add('lib')
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import Uid
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///location-ninja.db'
db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = "Event"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    location = db.Column(db.String(120), unique=False)

    def __init__ (self, name, location):
        self.id = Uid.uid_id_str()
        self.name = name
        self.location = location

    def __repr__(self):
        return 'Event %s @ %s' % (self.name, self.location)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/event/')
def event():
    try:
        temp = Event("Alpha 1", "Rondebosch")

        db.session.add(temp)
        db.session.commit()
    except Exception as e:
        print e.message
        return e.message
    return "success"

@app.route('/run/')
def user():
    try:
        records = Event.query.all()
        return str("<br/>".join(["%s @ %s" % (record.name, record.location) for record in records]))
    except Exception as e:
        return e.message



if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)