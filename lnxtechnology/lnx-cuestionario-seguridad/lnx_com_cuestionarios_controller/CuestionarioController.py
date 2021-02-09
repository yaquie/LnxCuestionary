# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, Blueprint
import mysql.connector
#from lnx_com_cuestionarios_model.Cuestionario import Cuestionario
#from lnx_com_cuestionarios_model.Response import Response
from lnx_com_cuestionarios_db.configuraciondb import db_conection


#app= Flask(__name__)
api = Blueprint('cuestionarios', __name__)

# https://www.nintyzeros.com/2019/11/flask-mysql-crud-restful-api.html


#http://localhost:3000/getQuestionByUser?id_seccion=4&id_usuario=1
@api.route('/getQuestionByUser')
def getQuestionByUser():
    try:
        id_seccion = request.args['id_seccion']
        id_usuario = request.args['id_usuario']
        
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
        
        lista =[]
        for x in data:
            lista.append(x)
        
        response = jsonify({"preguntas": data})
        
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()

#http://localhost:3000/getQuestionByUser2/1/1
@api.route('/getQuestionByUser2/<id_seccion>/<id_usuario>')
def getQuestionByUser2(id_seccion, id_usuario):
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
        
        lista =[]
        for x in data:
            lista.append(x)
        
        response = jsonify({"preguntas": lista})
        
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()
     
        
#http://localhost:3000/prueba?id_seccion=4&id_usuario=1     
@api.route('/prueba')
def invocando_metodo():
        lista = getQuestionByUser()
        print(type(lista))

 
  
 
@api.route('/atencion_sostenida/<int:id_seccion>')
def puntaje_atencion_sostenida(id_seccion):
    try:
        cur = db_conection.cursor()
        cur.execute("""
                    select p.id_pregunta, p.id_seccion, p.nro_pregunta, p.rpta_esperada, 
                    p.tiem_esperado, dp.rpta_realizada, dp.tiem_empleado 
                    from tbl03_pregunta p inner join tbl04_detalle_pregunta dp 
                    on p.id_pregunta = dp.id_pregunta
                    and p.id_seccion =%s
                    """ % (id_seccion))
        data = cur.fetchall()
        
        var_resultado = 0
        
        for pregunta in data:
            #id_pregunta = pregunta[0]
            #rpta_esperada = pregunta[5]
            var_seccion = pregunta[1]
            rpta_realizada = pregunta[5]
            var_resultado = var_resultado + int(rpta_realizada)
                
            
        var_dimension_cognitiva=""
        
        if var_resultado >= 0 and var_resultado  <=58:
            var_dimension_cognitiva='Bajo'
        elif var_resultado >= 59 and var_resultado <=67:
            var_dimension_cognitiva='Promedio Bajo'
        elif var_resultado >= 68 and var_resultado <=72:    
            var_dimension_cognitiva='Promedio'
        elif var_resultado >= 73 and var_resultado <=77:    
            var_dimension_cognitiva='Promedio Alto'
        else:
            var_dimension_cognitiva='Alto'
        
        response = jsonify({
                            "puntaje":var_resultado,
                            "dimension": var_dimension_cognitiva,
                            "seccion": var_seccion
                            })
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()
      
        
# retornar dimension por usuario y seccion      
@api.route('/atencion_dividida/<int:id_seccion>')
def puntaje_atencion_dividida(id_seccion):
    try:
        cur = db_conection.cursor()
        cur.execute("""
                    select p.id_pregunta, p.id_seccion, p.nro_pregunta, p.rpta_esperada, 
                    p.tiem_esperado, dp.rpta_realizada, dp.tiem_empleado 
                    from tbl03_pregunta p inner join tbl04_detalle_pregunta dp 
                    on p.id_pregunta = dp.id_pregunta
                    and p.id_seccion =%s """ % (id_seccion))
        data = cur.fetchall()
        
        var_resultado = 0
        var_dimension_cognitiva =""
        puntaje_obtenido=0
        nro_acierto = 0
        var_seccion = "atencion_dividida"
        
        if data[0][5] =='G':
            nro_acierto =1
            puntaje_obtenido += nro_acierto
        
        if data[1][5] =='4':
            nro_acierto =1
            puntaje_obtenido += nro_acierto
        
        if data[2][5] =='K':
            nro_acierto =1
            puntaje_obtenido += nro_acierto
        
        if data[3][5] =='7':
            nro_acierto =1
            puntaje_obtenido += nro_acierto
        
        
        # evaluacion de puntaje para asignar dimension
        if puntaje_obtenido >= 0 and puntaje_obtenido <= 2:
            var_dimension_cognitiva='Bajo'
        elif puntaje_obtenido == 3 :
            var_dimension_cognitiva='Promedio'
        else:
            var_dimension_cognitiva='Alto'
           
       
        response = jsonify({
                            "puntaje": puntaje_obtenido,
                            "dimension": var_dimension_cognitiva,
                            "seccion" : var_seccion
                            })
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()
  
    
#pendiente de implementar  
@api.route('/comprension_instrucciones/<int:id_seccion>')
def comprension_de_instrucciones(id_seccion):
    try:
        cur = db_conection.cursor()
        cur.execute("""
                    select p.id_pregunta, p.id_seccion, p.nro_pregunta, p.rpta_esperada, 
                    p.tiem_esperado, dp.rpta_realizada, dp.tiem_empleado 
                    from tbl03_pregunta p inner join tbl04_detalle_pregunta dp 
                    on p.id_pregunta = dp.id_pregunta
                    and p.id_seccion =%s
                    """ % (id_seccion))
        data = cur.fetchall()
        
        response = jsonify({
                            "puntaje":data
                            })
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()  
  
@api.route('/comprension_textos/<int:id_seccion>')
def puntaje_conprension_textos(id_seccion):
    try:
        cur = db_conection.cursor()
        cur.execute("""
                    select p.id_pregunta, p.id_seccion, p.nro_pregunta, p.rpta_esperada, 
                    p.tiem_esperado, dp.rpta_realizada, dp.tiem_empleado 
                    from tbl03_pregunta p inner join tbl04_detalle_pregunta dp 
                    on p.id_pregunta = dp.id_pregunta
                    and p.id_seccion =%s
                    """ % (id_seccion))
        data = cur.fetchall()
        
        #var_resultado = 0
        var_dimension_cognitiva =""
        var_seccion = "Comprension de Textos"
        puntaje_obtenido=0
        nro_acierto = 0
        
        
        #validacion de respuestas
        #pregunta1   -- ('b').lower()
        puntaje_obtenido +=1 if data[0][5]==('b').upper() else 0
                
        #pregunta2
        puntaje_obtenido +=1 if data[1][5]==('d').upper() else 0
                   
        #pregunta3
        puntaje_obtenido +=1 if data[2][5]==('c').upper() else 0
                   
        #pregunta4
        puntaje_obtenido +=1 if data[3][5]=='4,1,3,2' else 0
                  
        #pregunta5
        puntaje_obtenido +=1 if data[4][5]==('b').upper() else 0
                   
        #pregunta6
        puntaje_obtenido +=1 if data[5][5]==('c').upper() else 0
            
        #pregunta7
        puntaje_obtenido +=1 if data[6][5]==('d').upper() else 0
            
        
        # evaluacion de puntaje para asignar dimension
        if puntaje_obtenido >= 0 and puntaje_obtenido <= 3:
            var_dimension_cognitiva='Bajo'
        elif puntaje_obtenido == 4 or puntaje_obtenido == 5:
            var_dimension_cognitiva='Promedio'
        else:
            #puntaje_obtenido == 6 or 7
            var_dimension_cognitiva='Alto'
        
        response = jsonify({
                            "puntaje":puntaje_obtenido,
                            "dimension": var_dimension_cognitiva,
                            "seccion" : var_seccion
                            })
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()  
        
        
@api.route('/percepcion_riesgos/<int:id_seccion>')
def percepcion_riesgos(id_seccion):
    try:
        cur = db_conection.cursor()
        cur.execute("""
                    select p.id_pregunta, p.id_seccion, p.nro_pregunta, p.rpta_esperada, 
                    p.tiem_esperado, dp.rpta_realizada, dp.tiem_empleado 
                    from tbl03_pregunta p inner join tbl04_detalle_pregunta dp 
                    on p.id_pregunta = dp.id_pregunta
                    and p.id_seccion =%s
                    """ % (id_seccion))
        data = cur.fetchall()
        
        #var_resultado = 0
        var_dimension_cognitiva =""
        var_seccion = "Percepcion de Riesgos"
        puntaje_obtenido=0
        resultado = 0
        
        #validacion de respuestas
        #pregunta1   
        puntaje_obtenido +=1 if data[0][5] == ('0,1') else 0    
        #pregunta2
        puntaje_obtenido +=1 if data[1][5]==('1,0')else 0
        #pregunta3
        puntaje_obtenido +=1 if data[2][5]==('0,1') else 0
        #pregunta4
        puntaje_obtenido +=1 if data[3][5]==('1,0') else 0
        #pregunta5
        puntaje_obtenido +=1 if data[4][5]==('1,0') else 0
        #pregunta6
        puntaje_obtenido +=1 if data[5][5]==('1,0') else 0
        #pregunta7
        puntaje_obtenido +=1 if data[6][5]==('1,0') else 0
        
        # evaluacion de puntaje para asignar dimension
        if puntaje_obtenido >= 0 and puntaje_obtenido <= 5:
            var_dimension_cognitiva='Bajo'
        elif puntaje_obtenido == 6:
            var_dimension_cognitiva='Promedio'
        else:
            #puntaje_obtenido == 7
            var_dimension_cognitiva='Alto'
        
        
        response = jsonify({
                            "puntaje":puntaje_obtenido,
                            "dimension": var_dimension_cognitiva,
                            "seccion": var_seccion
                            })
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()  
        
#causas de Lesion
@api.route('/causas_lesion/<int:id_seccion>')
def causas_lesion(id_seccion):
    try:
        cur = db_conection.cursor()
        cur.execute("""
                    select p.id_pregunta, p.id_seccion, p.nro_pregunta, p.rpta_esperada, 
                    p.tiem_esperado, dp.rpta_realizada, dp.tiem_empleado 
                    from tbl03_pregunta p inner join tbl04_detalle_pregunta dp 
                    on p.id_pregunta = dp.id_pregunta
                    and p.id_seccion =%s
                    """ % (id_seccion))
        data = cur.fetchall()
        
        #var_resultado = 0
        var_dimension_cognitiva =""
        var_seccion = "Percepcion de Riesgos"
        puntaje_obtenido=0
        resultado = 0
        
        #validacion de respuestas
        #pregunta1   
        puntaje_obtenido +=1 if data[0][5] == ('0,1') else 0    
        #pregunta2
        puntaje_obtenido +=1 if data[1][5]==('1,0')else 0
        #pregunta3
        puntaje_obtenido +=1 if data[2][5]==('0,1') else 0
        #pregunta4
        puntaje_obtenido +=1 if data[3][5]==('1,0') else 0
        #pregunta5
        puntaje_obtenido +=1 if data[4][5]==('1,0') else 0
        #pregunta6
        puntaje_obtenido +=1 if data[5][5]==('1,0') else 0
        #pregunta7
        puntaje_obtenido +=1 if data[6][5]==('1,0') else 0
        
        # evaluacion de puntaje para asignar dimension
        if puntaje_obtenido >= 0 and puntaje_obtenido <= 5:
            var_dimension_cognitiva='Bajo'
        elif puntaje_obtenido == 6:
            var_dimension_cognitiva='Promedio'
        else:
            #puntaje_obtenido == 7
            var_dimension_cognitiva='Alto'
        
        
        response = jsonify({
                            "puntaje":puntaje_obtenido,
                            "dimension": var_dimension_cognitiva,
                            "seccion": var_seccion
                            })
        response.status_code=200
        return response
    except Exception as e:
        print(e)
    finally: 
        cur.close()  

@api.route('/add_question', methods = ['POST'])
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
        


@api.route('/update_question')
def update_contact():
    return 'update contact'


@api.route('/delete_contact')
def delete_contact():
    return 'delete contact'

@api.route('/saludo')
def saludo():
    response = jsonify({'resultado': 'OK'})
    return response


if __name__=='__main__':
    api.run(port=3000, debug=True)