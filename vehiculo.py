#-*- coding: utf-8 -*-
import datetime

class Vehiculo:
    def __init__ (self,placa="",marca="",modelo="",tipo="",hora_ingreso="",estado=""):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo=tipo
        self.hora_ingreso = hora_ingreso
        self.estado= True