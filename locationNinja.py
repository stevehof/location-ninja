import vendor
vendor.add('lib')

from flask import Flask, flash, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import forms
import Uid
import argparse
import os
import sys
#os.environ["SERVER_SOFTWARE"] = "Development/1"
app = Flask(__name__)
if len(sys.argv) > 1 and sys.argv[1] == "--dev":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///location-ninja.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+gaerdbms:///eastern-hawk-788:locationninjadb'
app.secret_key = 'why would I tell you my secret key?'
db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = "Event"
    id = db.Column(db.String, primary_key=True)
    course_name = db.Column(db.String(255), unique=False)
    course_province = db.Column(db.String(255), unique=False)
    contact_name = db.Column(db.String(255), unique=False)
    contact_email = db.Column(db.String(255), unique=False)
    contact_phone = db.Column(db.String(255), unique=False)
    alternate_contact_phone = db.Column(db.String(255), unique=False)
    course_website = db.Column(db.String(255), unique=False)
    course_type = db.Column(db.String(255), unique=False)
    denomination = db.Column(db.String(255), unique=False)
    language = db.Column(db.String(255), unique=False)
    venue_name = db.Column(db.String(255), unique=False)
    venue_location = db.Column(db.String(255), unique=False)
    venue_street = db.Column(db.String(255), unique=False)
    venue_suburb = db.Column(db.String(255), unique=False)
    venue_town = db.Column(db.String(255), unique=False)
    venue_postcode = db.Column(db.String(255), unique=False)
    venue_country = db.Column(db.String(255), unique=False)
    organisation_name = db.Column(db.String(255), unique=False)
    resources = db.Column(db.String(255), unique=False)
    gps_loc = db.Column(db.String(255), unique=False)
    courses_annual = db.Column(db.String(10), unique=False)
    course_email = db.Column(db.String(255), unique=False)
    leader_title = db.Column(db.String(255), unique=False)
    leader_name = db.Column(db.String(255), unique=False)
    leader_surname = db.Column(db.String(255), unique=False)
    leader_email = db.Column(db.String(255), unique=False)


    def __init__ (self, name, province):
        self.id = Uid.uid_id_str()
        self.course_name = name
        self.course_province = province

    def __repr__(self):
        return 'Event:%s %s @ %s' % (self.id, self.course_name, self.course_province)


@app.route('/')
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/try/', methods=['GET', 'POST'])
def event():
    form = forms.SearchForm(request.form)
    return render_template("try.html", form=form)

@app.route('/find/', methods=['GET', 'POST'])
def find():
    form = forms.SearchForm(request.form)
    if request.method == 'POST':
        return render_template("find.html", country=form.country.data, location=form.location.data)
    else:
        return render_template("try.html", form=form)

@app.route('/run/',  methods=['GET', 'POST'])
def user():
    form = forms.EventForm(request.form)
    if request.method == 'POST' and form.validate():
        event = Event(form.name.data, form.location.data)
        db.session.add(event)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('try'))
    return render_template("registerEvent.html",form=form)


@app.route('/display/', methods=['GET', 'POST'])
def display():
    events = db.session.query(Event).order_by(Event.course_name).limit(1).all()
    return render_template("display.html",records=events)

@app.route('/import/', methods=['GET', 'POST'])
def import_data_func():
    import importdata
    importdata.importdata()
    #os.environ["SERVER_SOFTWARE"] = "Prod/1"
    return "Success"



if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True,)#port=80)