import sqlalchemy_pervasive
import os 
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import pyodbc


Base=declarative_base()
engine = create_engine('pydobc:///ORB514810/demodata')

print('deez nuts')
# psquirrel = pyodbc.connect('Driver={Pervasive ODBC Interface};ServerName=Localhost;dbq=CONSTRUCDB2BDB0283')
# pcursor = psquirrel.cursor()

# pcursor.execute("""
#                 select xf$name from x$file

#                 """)

# prows = pcursor.fetchall()

# for row in prows:
#     print(row)

#for item in xrange(len(prows[1])):
#
#   print 'item %s is %s' % (item, prows[1][item])
    

print('massive chungus')