__author__ = 'steveh'
from sqlalchemy import String, Integer, Column

class Event(object):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    location = Column(String(120), unique=True)

    def __init__ (self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return 'Event %s @ %s' % (self.name, self.location)