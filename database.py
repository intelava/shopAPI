import flask_sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from sqlalchemy import Column, String, DateTime, Integer, DECIMAL
from sqlalchemy import create_engine, select, or_, types
import sqlite3
from datetime import datetime

from enum import Enum

engine = create_engine('sqlite:///database.db')#Session engine of sqlalchemy

from orderModels import Order
import objectModels


def insertRow(lst):

    session = Session(engine)
    for obj in lst:

        try:
            objectModels.insertFunc(obj, session)

        except:

            return "Bad request. One or more objects couldn't be inserted. Maybe you should make sure all attributes are defined, time format is D/M/Y H:M:S, you are inserting objects with an unique ID and in type of list.", 400



    return "Success!", 200



def getSession(databaseAddress):
    engine = create_engine(databaseAddress)

    session = Session(engine)

    return session