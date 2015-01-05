#!/usr/local/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Steve'

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
import re
import email


non_decimal = re.compile(r'[^\d.]+')
email_address = re.compile(r'[^@]+@[^@]+\.[^@]+')

engine = create_engine('sqlite:///location-ninja.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def importdata ():

    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from locationNinja import Event
    with open("data.csv","rb") as csvfile:
        records = csv.reader(csvfile,delimiter=";")
        next(records, None)
        for row in records:
            details = {}

            #Find or create new event
            assign_to_details(details, row)
            event = Event(details["course_name"], details["course_province"])
            existing_records = db_session.query(Event).filter(Event.course_name == details["course_name"], Event.course_province == details["course_province"])
            if existing_records.count() > 1:
                print "Duplicate rows found"
                print existing_records.all()
            elif existing_records.count() == 1:
                event = existing_records.first()

            #update event
            for col, value in details.iteritems():
                if value:
                    setattr(event, col, u_escape(value))

            db_session.add(event)
            print row[1]
            try:
                db_session.commit()
            except Exception as e:
                pass



    Base.metadata.create_all(bind=engine)


def assign_to_details(details, row):
    details["course_province"] = row[0]
    details["course_name"] = row[1]
    details["contact_name"] = row[2]
    details["contact_email"] = row[3] if re.match(email_address,row[3]) else ""
    details["contact_phone"], details["alternate_contact_phone"] = parsePhone(row[4])
    details["course_website"] = row[5]
    details["course_type"] = row[6]
    details["denomination"] = row[7]
    details["language"] = row[8]
    details["venue_name"] = row[9]
    details["venue_location"] = row[10]
    details["venue_street"] = row[11]
    details["venue_suburb"] = row[12]
    details["venue_town"] = row[13]
    details["venue_postcode"] = row[15]
    details["course_phone"] = row[16]
    details["venue_country"] = row[17]
    details["organisation_name"] = row[18]
    details["resources"] = u_escape(row[19])
    details["courses_annual"] = row[20]
    details["course_email"] = row[21] if re.match(email_address,row[21]) else ""
    details["leader_title"] = row[22]
    details["leader_name"] = row[23]
    details["leader_surname"] = row[24]
    details["leader_email"] = row[25] if re.match(email_address,row[25]) else ""

def parsePhone(value):
    numbers=value.split("/")
    return (non_decimal.sub('', numbers[0]) if len(numbers) else "", non_decimal.sub('', numbers[1]) if len(numbers) == 2 else "")

def u_escape(value):
    return value.decode('unicode_escape').encode('ascii','ignore')

if __name__ == "__main__":
    importdata()