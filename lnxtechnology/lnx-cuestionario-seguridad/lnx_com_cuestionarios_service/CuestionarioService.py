# -*- coding: utf-8 -*-

from modelo.Cuestionario import Cuestionario


def getResultados():
    resultado = Cuestionario('Atencion','1.1','1', 60, 45,8,5 )

    print(resultado.seccion)
    print(resultado.tarea)
    print(resultado.pregunta)
    print(resultado.tEstablecido)
    print(resultado.tEmpleado)
    print(resultado.rptaEsperada)
    print(resultado.rptaRealizada)

if __name__=='__main__':
    getResultados()
    
#rest
#https://danielsola.wordpress.com/2010/07/11/como-importar-clases-de-modulos-que-se-encuentran-en-diferente-directorio-en-python/
#https://www.paradigmadigital.com/dev/introduccion-django-rest-framework/
#https://github.com/paradigmadigital/demo-drf


