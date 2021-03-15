#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: monitor.py
# Capitulo: 3 Estilo Publica-Subscribe
# Autor(es): Perla Velasco, Yonathan Mtz & Team asd.
# Version: 2.0.2 Marzo 2021
# Descripción:
#
#   Ésta clase define el rol del monitor, es decir, muestra datos, alertas y advertencias sobre los signos vitales de los adultos mayores.
#
#   Las características de ésta clase son las siguientes:
#
#                                            monitor.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |        Monitor        |  - Mostrar datos a los  |         Ninguna        |
#           |                       |    usuarios finales.    |                        |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |  print_notification()  |  - datetime: fecha en que|  - Imprime el mensa-  |
#           |                        |     se envió el mensaje. |    je recibido.       |
#           |                        |  - id: identificador del |                       |
#           |                        |     dispositivo que      |                       |
#           |                        |     envió el mensaje.    |                       |
#           |                        |  - value: valor extremo  |                       |
#           |                        |     que se desea notifi- |                       |
#           |                        |     car.                 |                       |
#           |                        |  - name_param: signo vi- |                       |
#           |                        |     tal que se desea no- |                       |
#           +------------------------+--------------------------+-----------------------+
#           |   format_datetime()    |  - datetime: fecha que se|  - Formatea la fecha  |
#           |                        |     formateará.          |    en que se recibió  |
#           |                        |                          |    el mensaje.        |
#           +------------------------+--------------------------+-----------------------+
#           | print_accelorometer_data|  - datetime: fecha que se   |  - Imprime el     |
#           |                         |     formateará.             |    mensaje recibi-|
#           |                         |  - id: identificador del    |    do             |    
#           |                         |     dispositivo que envio   |                   |
#           |                         |     el mensaje              |                   |
#           |                         |  -valueX: Valor del eje X   |                   |
#           |                         |  -valueY: Valor del eje Y   |                   |
#           |                         |  -valueZ: Valor del eje Z   |                   |
#           |                         |  -name_param: tipo de objeto|                   |
#           |                         |  -model = Modelo de la My   |                   |
#           |                         |           Band.             |                   |
#           +-------------------------+-----------------------------+-------------------+
#           +------------------------+--------------------------+-----------------------+
#           | print_medicament_alert  |  - datetime: fecha que se   |  - Imprime la     |
#           |                         |     formateará.             |    alerta recibi- |
#           |                         |  - id: identificador del    |    da             |    
#           |                         |     dispositivo que envio   |                   |
#           |                         |     el mensaje              |                   |
#           |                         |  -med_name: nombre del medi-|                   |
#           |                         |   camento.                  |                   |
#           |                         |  -dosis:porcion de medica-  |                   |
#           |                         |   mento a sumistrar.        |                   |
#           |                         |  -model = Modelo de la My   |                   |
#           |                         |           Band.             |                   |
#           +-------------------------+-----------------------------+-------------------+



class Monitor:

    def print_notification(self, datetime, id, value, name_param, model):
        print("  ---------------------------------------------------")
        print("    ADVERTENCIA")
        print("  ---------------------------------------------------")
        print("    Se ha detectado un incremento de " + str(name_param) + " (" + str(value) + ")" + " a las " + str(self.format_datetime(datetime)) + " en el adulto mayor que utiliza el dispositivo " + str(model) + ":" + str(id))
        print("")
        print("")

    def print_accelerometer_data(self, datetime, id, valueX, valueY, valueZ, name_param, model):
        print("  ---------------------------------------------------")
        print("    ADVERTENCIA")
        print("  ---------------------------------------------------")
        print("    Se ha detectado un cambio en "+str(name_param)+" del adulto mayor que tiene el modelo "+str(model)+" y la id "+str(id)+": \n"+"X: "+str(valueX)+"\n"+"Y: "+str(valueY)+"\n"+"Z: "+str(valueZ)+"\nen "+str(datetime))
        print("")
        print("")

    def print_medicament_alert(self,datetime,id,type,med_name,dosis,model):
        print("  ---------------------------------------------------")
        print("    ADVERTENCIA")
        print("  ---------------------------------------------------")
        print("    Es hora de aplicar el medicamento  ("+str(datetime)+") "+str(med_name)+", con dosis de "+str(dosis)+" en el adulto que utiliza el dispositivo "+str(model)+":"+str(id))
        print("")
        print("")

    def format_datetime(self, datetime):
        values_datetime = datetime.split(':')
        f_datetime = values_datetime[3] + ":" + values_datetime[4] + " del " + \
            values_datetime[0] + "/" + \
            values_datetime[1] + "/" + values_datetime[2]
        return f_datetime
