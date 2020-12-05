# -*- coding: utf-8 -*-
# ejemplo clases: https://www.w3schools.com/python/python_classes.asp
#https://python-para-impacientes.blogspot.com/2015/06/programacion-orientada-objetos-y-iii.html

class Cuestionario:
    def __init__(self, seccion, tarea, pregunta, tEstablecido, tEmpleado, rptaEsperada, rptaRealizada):
        self.seccion = seccion
        self.tarea = tarea
        self.pregunta = pregunta
        self.tEstablecido = tEstablecido
        self.tEmpleado = tEmpleado
        self.rptaEsperada = rptaEsperada
        self.rptaRealizada = rptaRealizada

    def getSeccion(self):
        return self.seccion

    def setSeccion(self, seccion):
        self.seccion = seccion
        
    def getTarea(self):
        return self.tarea

    def setTarea(self, tarea):
        self.tarea = tarea
        
    def getPregunta(self):
        return self.pregunta

    def setPregunta(self, pregunta):
        self.pregunta = pregunta
        
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
        
