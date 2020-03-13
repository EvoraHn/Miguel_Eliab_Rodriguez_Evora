#-*- coding: utf-8 
from vehiculo import Vehiculo
class Estacionamiento:
    def __init__(self):
        """ Inicializa un estacionamiento Vacío """
        self.vehiculos = list()
    
    def Guardar(self,placa="",marca="",modelo="",tipo="",hora_ingreso="",estado=""):
        """ Agrega un nuevo elmento al estacionamiento """
        self.vehiculos.append(Vehiculo(placa,marca,modelo,tipo,hora_ingreso,estado))


