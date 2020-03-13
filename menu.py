#-*- coding: utf-8 -*-
#programa : Estacionamiento
#Objetivo : Simular un estacionamiento 
#Autor Eliab Evora
#Fecha: 13/03/2020
from datetime import datetime, timedelta
import sys
import platform
from estacionamiento import Estacionamiento
class Menu:
    def __init__(self):
        """Inicializa el programa de estacionamiento"""
        self.estacionamiento = Estacionamiento()
        self.opciones= {
            "1":self.Ingresar_Vehiculo,
            "2":self.despachar_Vehiculo,
            "3":self.resumen_Ingresado,
            "4":self.resumen_salido,
            "5":self.resumen_ganancia,
            "6":self.salir
        }

    def desplegar_menu(self):
        """Despliega el menu de interacción del Usuario"""
        print("""
            -*-*-*-Menu-*-*-*-
            
             opciones: 
                        1.Ingresar Vehiculo
                        2.despachar Vehiculo
                        3.Resumen Vehiculos Ingresados
                        4.Resumen Vehiculos Despachados
                        5.Resumen Ganancia
                        6.Salir
                        """)
    def run(self):
        """Ejecuta el programa en un ciclo"""
        while True:
            self.desplegar_menu()
            seleccion = input("Elija Una Opción: ")
            accion = self.opciones.get(seleccion)

            if accion:
                accion()
            else:
                print("Opcion invalida")

    def Ingresar_Vehiculo(self):
        """Registra Un vehiculo al ingresar en el estacionamiento"""
        placa = input ("Ingrese la placa del vehículo: ")
        marca = input ("Ingrese la marca del vehículo: ")
        modelo = input ("Ingrese el modelo del vehículo: ")
        tipo = input ("Ingrese el tipo de vehículo: (1.carro o 2.moto)")
        plus_five_hours = datetime.now() 
        #placa = input ("Ingrese la placa del vehículo")
        self.estacionamiento.guardar(placa,marca,modelo,tipo,plus_five_hours)

    def resumen_Ingresado(self):
        """ Retorna una lista de vehiculos ingresados"""
        self.estacionamiento.ver_Resumen(True)
        
    def resumen_salido(self):
        """Retorna una lista de vehiculos que ya no se encuentran 
        alojados dentro del estacionamiento"""
        self.estacionamiento.ver_Resumen(False)

    def despachar_Vehiculo(self):
        placa = input ("""ingrese el número de placa del vehiculo 
        que va a despachar: """)
        hora_salida = datetime.now() + timedelta(hours=5)
        self.estacionamiento.despachar(placa,hora_salida)
    
    
    def salir(self):
        """Cierra la app"""
        sys.exit(0)
    
    def resumen_ganancia(self):
        self.estacionamiento.gana()

if __name__ == "__main__":
    menu = Menu()
    menu.run()    
  

