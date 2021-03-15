#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: procesador_de_medicamentos.py
# Capitulo: 3 Estilo Publica-Subscribe
# Autor(es): Perla Velasco, Yonathan Mtz & Team asd.
# Version: 2.0.2 Marzo 2021
# Descripción:
#
#   Esta clase define el rol de un suscriptor, es decir, es un componente que recibe mensajes.
#
#   Las características de ésta clase son las siguientes:
#
#                                     procesador_de_medicamentos.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Se suscribe a los   |
#           |                       |                         |    eventos generados   |
#           |                       |  - Procesa los horarios |    por el wearable     |
#           |     Procesador de     |  para la administración |    Xiaomi My Band.     |
#           |        medicamentos   |   de medicamentos       |                        |
#           |                       |                         |  - Notifica al monitor |
#           |                       |                         |    cuando es hora de   |
#           |                       |                         |    sumistrar algun medicamento.|
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                               Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Recibe la hora     |
#           |       consume()        |          Ninguno         |    actual del Xiaomi  |
#           |                        |                          |    My Band            |
#           |                        |                          |                       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |  - ch: propio de Rabbit. |  - Detecta si en la hora |
#           |                        |  - method: propio de     |   actual hay algun    |
#           |                        |     Rabbit.              |   medicmamento que deba|
#           |       callback()       |  - properties: propio de |   suminstrarse y      |       
#           |                        |     Rabbit.              |   notifica al monitor |
#           |                        |  - body: mensaje recibi- |                       |
#           |                        |     do.                  |                       |
#           +------------------------+--------------------------+-----------------------+
#           |    string_to_json()    |  - string: texto a con-  |  - Convierte un string|
#           |                        |     vertir en JSON.      |    en un objeto JSON. |
#           +------------------------+--------------------------+-----------------------+
#
#
#           Nota: "propio de Rabbit" implica que se utilizan de manera interna para realizar
#            de manera correcta la recepcion de datos, para éste ejemplo no shubo necesidad
#            de utilizarlos y para evitar la sobrecarga de información se han omitido sus
#            detalles. Para más información acerca del funcionamiento interno de RabbitMQ
#            puedes visitar: https://www.rabbitmq.com/
#
#-------------------------------------------------------------------------
import pika
import random
import sys
sys.path.append('../')
from monitor import Monitor
import time


class ProcesadorMedicamento:
    medicamentos=[
        'Paracetamol',
        'Ibuprofeno',
        'Insulina'
    ]
    horarios_medicamentos=[
        '08',
        '12',
        '06'
    ]
    
    def consume(self):
        try:
            # Se establece la conexión con el Distribuidor de Mensajes
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
            # Se solicita un canal por el cuál se enviarán los signos vitales
            channel = connection.channel()
            # Se declara una cola para leer los mensajes enviados por el
            # Publicador
            channel.queue_declare(queue='time', durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(on_message_callback=self.callback, queue='time')
            channel.start_consuming()  # Se realiza la suscripción en el Distribuidor de Mensajes
        except (KeyboardInterrupt, SystemExit):
            channel.close()  # Se cierra la conexión
            sys.exit("Conexión finalizada...")
            time.sleep(1)
            sys.exit("Programa terminado...")

    def callback(self, ch, method, properties, body):
        json_message = self.string_to_json(body)
        hora= str(json_message['time']).split(":")
        monitor=Monitor()
        
        medicament_id = random.randint(0,2)
        dosis= random.randint(10,500)
        
        medicamento = self.medicamentos[medicament_id]
        horario = self.horarios_medicamentos[medicament_id]
        
        ## si la hora es las 12:00 am, en el formato que lo regresa el My band es 00:00, en este caso, la cambiamos por un 24.
        if hora[0]=='00':
            hora[0] ='24'

        if int(hora[0]) % int(horario) == 0 and hora[1] == "00":
            monitor.print_medicament_alert(json_message['datetime'],json_message['id'],'Medicamento',medicamento,dosis,json_message['model'])
            
        time.sleep(1)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def string_to_json(self, string):
        message = {}
        string = string.decode('utf-8')
        string = string.replace('{', '')
        string = string.replace('}', '')
        values = string.split(', ')
        for x in values:
            v = x.split(': ')
            message[v[0].replace('\'', '')] = v[1].replace('\'', '')
        return message

if __name__ == '__main__':
    p_medicamentos = ProcesadorMedicamento()
    p_medicamentos.consume()
