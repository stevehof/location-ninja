import vendor
vendor.add('lib')

from flask import Flask, flash, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import forms
import Uid
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///location-ninja.db'
app.secret_key = 'why would I tell you my secret key?'
db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = "Event"
    id = db.Column(db.String, primary_key=True)
    course_name = db.Column(db.String(80), unique=False)
    course_province = db.Column(db.String(120), unique=False)
    primary_contact_name = db.Column(db.String(120), unique=False)
    primary_contact_email = db.Column(db.String(120), unique=False)
    primary_contact_phone = db.Column(db.String(120), unique=False)
    course_website = db.Column(db.String(120), unique=False)
    course_type = db.Column(db.String(120), unique=False)
    denomination = db.Column(db.String(120), unique=False)
    language = db.Column(db.String(120), unique=False)
    venue_name = db.Column(db.String(120), unique=False)
    venue_location = db.Column(db.String(255), unique=False)
    venue_street = db.Column(db.String(120), unique=False)
    venue_suburb = db.Column(db.String(120), unique=False)
    venue_town = db.Column(db.String(120), unique=False)
    venue_postcode = db.Column(db.String(120), unique=False)
    venue_country = db.Column(db.String(120), unique=False)
    organisation_name = db.Column(db.String(120), unique=False)
    resources = db.Column(db.String(255), unique=False)
    gps_loc = db.Column(db.String(255), unique=False)


    def __init__ (self, name, location):
        self.id = Uid.uid_id_str()
        self.name = name
        self.location = location

    def __repr__(self):
        return 'Event %s @ %s' % (self.course_name, self.course_province)


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



if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)