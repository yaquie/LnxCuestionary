# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import mysql.connector
#from lnx_com_cuestionarios_model.Cuestionario import Cuestionario
#from lnx_com_cuestionarios_model.Response import Response
from lnx_com_cuestionarios_controller.CuestionarioController import api

app= Flask(__name__)


@app.route('/')
def principal():
    return jsonify({"message" : "welcome to LnxTechnology"})

#invocando al modulo controller
app.register_blueprint(api)

if __name__=='__main__':
    app.run(port=3000, debug=True)