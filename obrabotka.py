#!/usr/bin/env python3

import cgi

our_form = cgi.FieldStorage()

autoname = our_form.getfirst("autoname", "не задано")
nomer = our_form.getfirst("nomer", "не задано")

import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error
#print(f)
try:
    with connect(
        host="localhost",
        user='root',
        password='admin1',
        database = "avtomobil",
    ) as connection:
        dobav = f"insert into new_table (marka, a_nomer) values ('{autoname}', '{nomer}') "
        with connection.cursor() as cursor:
            cursor.execute(dobav)
            connection.commit()
            print('all right')
except Error as e:
    print(e)
print("Content-type: text/html")
print()


