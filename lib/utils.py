#!/usr/bin/env python
# coding: utf-8

"""
This file is part of web2py Web Framework (Copyrighted, 2007-2009).
Developed by Massimo Di Pierro <mdipierro@cs.depaul.edu>.
License: GPL v2
"""

import hashlib

def md5_hash(text):
    """ Generate a md5 hash with the given text """

    return hashlib.md5(text).hexdigest()


def hash(text, digest_alg = 'md5'):
    """
    Generates hash with the given text using the specified 
    digest hashing algorithm 
    """    
    h = hashlib.new(digest_alg)
    h.update(text)
    return h.hexdigest()
