"""
This file is part of web2py Web Framework (Copyrighted, 2007-2009).
Developed by Massimo Di Pierro <mdipierro@cs.depaul.edu>.
License: GPL v2
"""
import datetime
from storage import Storage
import simplejson

def json(value):
    return simplejson.dumps(value)

def csv(value):
    return ''
