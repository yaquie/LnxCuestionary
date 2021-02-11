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


#@api.route('/add_question', methods = ['POST'])
def add_question():
    try:
        _json = request.json
        _id_pregunta = _json['id_pregunta']
        _id_usuario = _json['id_usuario']
        _rpta_realizada = _json['rpta_realizada']
        _tiemp_empleado = _json['tiem_empleado']
        _estado = _json['estado']
                 
        sql_query = ("""
                     INSERT INTO tbl04_detalle_pregunta
                     (id_pregunta, id_usuario, rpta_realizada, tiem_empleado, estado, fec_crea)
                     VALUES (%s, %s, %s, %s, %s, now())
                     """)
        param_input = (_id_pregunta, _id_usuario, _rpta_realizada, _tiemp_empleado, _estado)
        
        cur = db_conection.cursor()
        cur.execute(sql_query, param_input)
        
        db_conection.commit()
        print(cur.rowcount, "Registro exitoso")
        #response = jsonify('Registro exitoso')
        #response.status_code = 200
        #return response
    
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


