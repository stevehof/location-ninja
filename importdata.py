#!/usr/local/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Steve'

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
import re

non_decimal = re.compile(r'[^\d.]+')

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
        for row in records:
            print parsePhone(row[16])

    Base.metadata.create_all(bind=engine)


def parsePhone(value):
    return non_decimal.sub('', value)


if __name__ == "__main__":
    importdata()