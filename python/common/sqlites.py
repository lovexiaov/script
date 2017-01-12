# coding: utf-8
"""
This module demonstrate how to use sqlite3.
"""
__author__ = u'lovexiaov'

import sqlite3

db = sqlite3.connect('test.db') # open sqlite db
def create_table():
    sql = ''' CREATE TABLE person
        (_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        addr CHAR(50));'''
    db.execute(sql) # create table

def insert():
    sql = '''INSERT INTO person (name, age, addr) 
        VALUES ('lovexiaov', 23, 'chaoyang, beijing');'''
    db.execute(sql)
    db.commit()

def query():
    sql = '''SELECT _id, name FROM person;'''
    cursor = db.execute(sql)
    for row in cursor:
        print('id: %s, name: %s' %row)

def update():
    sql = '''UPDATE person SET name = "zhangsan" WHERE _id = 1;'''
    db.execute(sql)
    db.commit()
    query()

def delete():
    sql = '''DELETE FROM person where name = "lovexiaov";'''
    db.execute(sql)
    db.commit()
    
if __name__ == u'__main__':
    # create_table()
    # insert()
    # query()
    # update()
    insert()
    query()
    print('==='*3)
    delete()
    query()
    db.close()