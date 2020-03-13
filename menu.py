#-*- coding: utf-8 -*-
#programa : Estacionamiento
#Objetivo : Simular un estacionamiento 
#Autor Eliab Evora
#Fecha: 13/03/2020

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
            "5":self.resumen:ganancia,
            "6":self.salir
        }

        def desplegar_menu():
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

