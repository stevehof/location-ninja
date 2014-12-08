__author__ = 'Steve'

from wtforms import Form, StringField, validators


class EventForm(Form):
    name = StringField(u'Name', validators=[validators.input_required()])
    location  = StringField(u'Location', validators=[validators.optional()])