# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 15:10:33 2018

@author: John sippy
"""
import psycopg2

def connect_to_db():
    con=psycopg2.connect(dbname= '', host='', port= '5439', user= '', password= '')
    return con	

