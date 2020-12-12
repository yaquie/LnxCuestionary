# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:37:15 2020

@author: JAKIE
"""

# ejemplo clases: https://www.w3schools.com/python/python_classes.asp
#https://python-para-impacientes.blogspot.com/2015/06/programacion-orientada-objetos-y-iii.html

class Cuestionario:
    
    def __init__(self, id_pregunta, id_seccion, nro_tarea, nro_pregunta, 
                 tEstablecido, tEmpleado, rptaEsperada, rptaRealizada):
        self.id_pregunta=id_pregunta
        self.id_seccion = id_seccion
        self.nro_tarea = nro_tarea
        self.nro_pregunta = nro_pregunta
        self.tEstablecido = tEstablecido
        self.tEmpleado = tEmpleado
        self.rptaEsperada = rptaEsperada
        self.rptaRealizada = rptaRealizada

    def getIdPregunta(self):
        return self.getIdPregunta
    
    def setIdPregunta(self, id_pregunta):
        self.id_pregunta = id_pregunta

    def getIdSeccion(self):
        return self.id_seccion

    def setSeccion(self, id_seccion):
        self.id_seccion = id_seccion
        
    def getNroTarea(self):
        return self.nro_tarea

    def setNroTarea(self, nro_tarea):
        self.nro_tarea = nro_tarea
        
    def getNroPregunta(self):
        return self.nro_pregunta

    def setNroPregunta(self, nro_pregunta):
        self.nro_pregunta = nro_pregunta
        
    def getTEstablecido(self):
        return self.tEstablecido

    def setTEstablecido(self, tEstablecido):
        self.tEstablecido = tEstablecido
        
    def getTEmpleado(self):
        return self.tEmpleado

    def setTEmpleado(self, tEmpleado):
        self.tEmpleado = tEmpleado
        
    def getRptaEsperada(self):
        return self.rptaEsperada

    def setRptaEsperada(self, rptaEsperada):
        self.rptaEsperada = rptaEsperada
        
    def getRptaRealizada(self):
        return self.rptaRealizada

    def setRptaRealizada(self, rptaRealizada):
        self.rptaRealizada = rptaRealizada
        
q1 = Cuestionario(1, 'Atencion Sostenida', 'T.1.1', '1', '60 seg', '60 seg', 57, 54)
q2 = Cuestionario(2, 'Atencion Dividida', 'T.2.1', '1', '60 seg', '60 seg', 4, 3)
q3 = Cuestionario(3, 'Percepcion de riesgos', 'T.4.1', '1', '60 seg', '60 seg', 4, 3)

question_list = []
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)

#for i in question_list:
#   print(i.getIdSeccion())




