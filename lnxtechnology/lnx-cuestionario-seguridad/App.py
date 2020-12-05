# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import mysql.connector
from lnx_com_cuestionarios_model.Cuestionario import Cuestionario


app= Flask(__name__)
#app.config['MYSQL_HOST']= 'localhost'
#app.config['MYSQL_USER']= 'root'
#app.config['MYSQL_PASSWORD']= 'admin'
#app.config['MYSQL_DB']= 'lnxtechnologydb'
#mysql =mysql.connector.connect(app)

db_conection = mysql.connector.connect( host='localhost', 
                                         user='root', 
                                         passwd='admin', 
                                         db='lnxtechnologydb')

# https://www.nintyzeros.com/2019/11/flask-mysql-crud-restful-api.html

@app.route('/questions')
def list_questions():
    try:
        cur = db_conection.cursor()
        cur.execute( "select p.id_pregunta, p.id_seccion, p.nro_tarea,dp.nro_pregunta,  dp.rpta_esperada, dp.rpta_realizada, dp.tpo_esperado, dp.tpo_empleado from tbl02_detalle_pregunta dp inner join tbl01_pregunta p on dp.id_pregunta =p.id_pregunta and p.estado='1' and dp.estado='1'" )
        data = cur.fetchall()
        response = jsonify({"preguntas": data})
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()
  
@app.route('/get_question/<int:id_pregunta>')  
def get_question(id_pregunta):
    
    try:
        cur = db_conection.cursor()
        cur.execute("select p.id_pregunta, p.id_seccion, p.nro_tarea,dp.nro_pregunta,  dp.rpta_esperada, dp.rpta_realizada, dp.tpo_esperado, dp.tpo_empleado from tbl02_detalle_pregunta dp inner join tbl01_pregunta p on dp.id_pregunta =p.id_pregunta and p.estado='1' and dp.estado='1' and p.id_pregunta=%s" % (id_pregunta))
        pregunta = cur.fetchmany()
        response = jsonify({"pregunta": pregunta})
        return response
    except Exception as e:
        print(e)
    finally:
        cur.close()


@app.route('/add_question', methods = ['POST'])
def add_question():
    try:
        _json = request.json
        _id_seccion = _json['id_seccion']
        _nro_tarea = _json['nro_tarea']
        _estado = _json['estado']
        sql_query = ("INSERT INTO tbl01_pregunta(id_seccion,nro_tarea,estado, fec_crea) VALUES(%s, %s, %s, now())")
        bind_data = (_id_seccion, _nro_tarea, _estado)
        cur = db_conection.cursor()
        
        cur.execute(sql_query, bind_data)
        db_conection.commit()
        response = jsonify('Registro exitoso')
        response.status_code = 200
        return response
    
    except Exception as e:
        print(e)
    finally:
        cur.close()
        db_conection.close()
        


@app.route('/update_question')
def update_contact():
    return 'update contact'


@app.route('/delete_contact')
def delete_contact():
    return 'delete contact'

if __name__=='__main__':
    app.run(port=3000, debug=True)

