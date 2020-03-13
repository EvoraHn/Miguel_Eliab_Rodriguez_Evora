#-*- coding: utf-8 
from vehiculo import Vehiculo
class Estacionamiento:
    def __init__(self):
        """ Inicializa un estacionamiento Vacío """
        self.vehiculos = list()
        self.ganancias = list()
    
    def guardar(self,placa="",marca="",modelo="",tipo="",hora_ingreso="",estado=""):
        """ Agrega un nuevo elmento al estacionamiento """
        self.vehiculos.append(Vehiculo(placa,marca,modelo,tipo,hora_ingreso,estado))

    def ver_Resumen(self,valor):
        """Retorna un reporte dependiendo el valor"""
        for x in range(len(self.vehiculos)):
            if valor == self.vehiculos[x].estado:
                print ("""Placa: {0}\nMarca: {1} \nModelo: {2} \nTipo: {3} 
                    \nHora de entrada: {4} \n Estado: {5}""".format(self.vehiculos[x].placa,
                    self.vehiculos[x].marca,self.vehiculos[x].modelo,self.vehiculos[x].tipo,
                    self.vehiculos[x].hora_ingreso,self.vehiculos[x].estado))
                    

    def despachar(self, placa, hora_salida):
        """Retorna el ticket cuando el cliente se va"""
        for x in range(len(self.vehiculos)):
            if placa == self.vehiculos[x].placa:
                calculo = (20 + ((4*20)-((4*20)*0.20)))
                print (""" *- Gracias por Utilizar Nuestro Parqueo -*\n
                Placa: {0}\nMarca: {1} \nModelo: {2} \nTipo: {3} 
                    \nHora de entrada: {4} \nHora de salida: {6} \nEstado: {5} \n Total a pagar: {7}""".format(self.vehiculos[x].placa,
                    self.vehiculos[x].marca,self.vehiculos[x].modelo,self.vehiculos[x].tipo,
                    self.vehiculos[x].hora_ingreso,hora_salida,self.vehiculos[x].estado,calculo))
                    #ganancias.append(calculo)
            else:
                print("el vehiculo no existe dentro el almacenamiento")

    def gana(self):
        #print(self.ganancias)
        pass

