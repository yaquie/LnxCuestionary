# -*- coding: utf-8 -*-

from Main_App import app
import mysql.connector


mysql = mysql.connector

app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'admin'
app.config['MYSQL_DB']= 'lnxtechnologydb'

mysql.Connect(app)




