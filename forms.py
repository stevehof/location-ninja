__author__ = 'Steve'

from wtforms import Form, StringField, validators, TextField, SelectField, SelectMultipleField, IntegerField


class EventForm(Form):
    course_name = StringField(u'Name', validators=[validators.input_required()])
    course_province = StringField(u'Location', validators=[validators.optional()])
    primary_contact_name = StringField(u'Contact Name', validators=[validators.input_required()])
    primary_contact_email = StringField(u'Contact Email', validators=[validators.input_required()])
    primary_contact_phone = StringField(u'Contact Number', validators=[validators.input_required()])
    course_website = StringField(u'Website')
    course_type = SelectField(u'Course Type', validators=[validators.input_required()],
                              choices=(("alpha", "Alpha"), ("youthalpha", "Alpha for Youth")))
    denomination = StringField(u'Denomination')
    language = StringField(u'Main Language', validators=[validators.input_required()])
    venue_name = StringField(u'Venue Name', validators=[validators.input_required()])
    venue_location = StringField(u'House Name/Number', validators=[validators.input_required()])
    venue_street = StringField(u'Street', validators=[validators.input_required()])
    venue_suburb = StringField(u'Suburb')
    venue_town = StringField(u'Town/City', validators=[validators.input_required()])
    venue_postcode = IntegerField(u'Postcode')
    venue_country = SelectField(u'Country', validators=[validators.input_required()])
    gps_loc = StringField(u'GPS Location')
    organisation_name = StringField(u'Organisation Name', validators=[validators.input_required()])
    resources = SelectMultipleField(u'Resources', validators=[validators.input_required()])

class SearchForm(Form):
    countries = (("ZA", "South Africa"),)
    country = SelectField(u'Country', validators=[validators.input_required()], choices=countries, id="try-country")
    location = StringField(u'Location', validators=[validators.optional()], id="try-postcode", default="Cape Town")