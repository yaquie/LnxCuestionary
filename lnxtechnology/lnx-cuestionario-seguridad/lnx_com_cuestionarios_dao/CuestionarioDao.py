# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, Blueprint
import mysql.connector
from lnx_com_cuestionarios_db.configuraciondb import db_conection


api = Blueprint('cuestionariosDao', __name__)

# metodo - ok
#http://localhost:3000/getQuestionByUser2/1/1
def getQuestionByUser(id_seccion, id_usuario):
    try:
                
        query = """
                    select p.id_pregunta, p.id_seccion, p.nro_pregunta, p.rpta_esperada, 
                    p.tiem_esperado, dp.rpta_realizada, dp.tiem_empleado 
                    from tbl03_pregunta p inner join tbl04_detalle_pregunta dp 
                    on p.id_pregunta = dp.id_pregunta
                    and p.id_seccion = %s
                    and dp.id_usuario = %s
                    """ 
        input_parameters =(id_seccion, id_usuario)
        
        cur = db_conection.cursor()
        cur.execute(query, input_parameters)                  
        data = cur.fetchall()
        
        return data
    except Exception as e:
        print(e)
    finally: 
        cur.close()

# link rest api crud example
#https://medium.com/@hamdi.fersi/python-rest-api-crud-example-using-flask-and-mysql-8211c49c27d4
#@api.route('/add_question', methods = ['POST'])
def add_question(_id_pregunta, _id_usuario, _rpta_realizada, _tiemp_empleado, _estado ):
    try:
                        
        sql_query = ("""
                     INSERT INTO tbl04_detalle_pregunta
                     (id_pregunta, id_usuario, rpta_realizada, tiem_empleado, estado, fec_crea)
                     VALUES (%s, %s, %s, %s, %s, now())
                     """)
        param_input = (_id_pregunta, _id_usuario, _rpta_realizada, _tiemp_empleado, _estado)
        
        cur = db_conection.cursor()
        cur.execute(sql_query, param_input)
        
        db_conection.commit()
        
        data = cur.lastrowid
        
        mensaje = ''
        codigo  = ''
        if data is None :
            mensaje = 'Error en el registro'
            codigo = '01'
            return  mensaje, codigo
        else:
            mensaje = 'Registro exitoso'
            codigo = '00'
            return  mensaje, codigo

    except Exception as e:
        print(e)
    finally:
        cur.close()
        db_conection.close()
        


#@api.route('/update_question')
def update_contact():
    return 'update contact'


#@api.route('/delete_contact')
def delete_contact():
    return 'delete contact'

#@api.route('/saludo')
def saludo():
    #response = jsonify({'resultado': 'OK'})
    response ='saludo cuestionario DAO'
    return response


