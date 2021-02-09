# -*- coding: utf-8 -*-

#from Main_App import app 
import mysql.connector
from flask import Blueprint


#db_conection = Blueprint('configuracionBD', __name__)

try:
    db_conection = mysql.connector.connect( host='localhost', 
                                         user='root', 
                                         passwd='admin', 
                                         db='lnxtechnologydb_2')
    print('conexion exitosa')
except(mysql.connector.errorcode, mysql.connector.InternalError) as e:
    print('Error en la conexion de bd', e)
    

