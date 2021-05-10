import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime


def on_connect(client, userdata, flags, rc):
    print('conectado publicador')


def main():
    client = paho.mqtt.client.Client("Unimet", False)
    client.qos = 0
    client.connect(host='localhost')
    cantHoras = 24
    hora = 0
    cantidadDeDispositivos = 5
    horaBase= datetime.datetime.now().replace(minute=0, second=0)

    mean_temp_nevera = 10
    std_temp_nevera = 2

    while(cantHoras>hora):
        hora+=1
        horaBase = horaBase + datetime.timedelta(hours=1) 
        while(cantidadDeDispositivos > 0):
            temperatura_nevera = int(np.random.normal(mean_temp_nevera,std_temp_nevera))
            capacidad_hielo_nevera = int(np.random.uniform(0,10))

            horas = horaBase + datetime.timedelta(minutes=5)

            payload = {

                "fecha": str(horas),
                "Temperatura de la Nevera": temperatura_nevera,
                "Capacida de Generar Hielo en la Nevera": capacidad_hielo_nevera,
            }

            client.publish('unimet/admin/bd',json.dumps(payload),qos=0)	


            cantidadDeDispositivos -= 1
            print(payload)
            time.sleep(0.5)
        cantidadDeDispositivos = 5


if __name__ == '__main__':
    main()
sys.exit(0)