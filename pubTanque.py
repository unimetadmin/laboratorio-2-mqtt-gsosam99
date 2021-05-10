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

    mean_percent_ent_tanque = 10
    std_percent_ent_tanque = 5
    mean_percent_sal_tanque = 20
    std_percent_sal_tanque = 5
    nivel_tanque = 100

    while(cantHoras>hora):
        hora+=1
        horaBase = horaBase + datetime.timedelta(hours=1) 
        while(cantidadDeDispositivos > 0):

            ## Cada 10 min
            nivel_tanque -= int(np.random.normal(mean_percent_ent_tanque,std_percent_ent_tanque))
            ##

            ## Cada 30 min
            nivel_tanque += int(np.random.normal(mean_percent_sal_tanque,std_percent_sal_tanque))
            ##

            horas = horaBase + datetime.timedelta(minutes=np.random.uniform(0,60))

            payload = {
                "fecha": str(horas),
                "Nivel del tanque de Agua": nivel_tanque,
            }

            client.publish('unimet/admin/bd',json.dumps(payload),qos=0)	

            ##Cada 10 minutos
            if nivel_tanque == 50:
                print("El nivel de agua en el tanque esta por la mitad")
            elif nivel_tanque < 50 and nivel_tanque > 0:
                print("El nivel de agua en el tanque esta por debajo de la mitad")
            elif (nivel_tanque == 0):
                print("El tanque de agua esta vacio")
            ##

            cantidadDeDispositivos -= 1
            print(payload)
            time.sleep(0.5)
        cantidadDeDispositivos = 5


if __name__ == '__main__':
    main()
sys.exit(0)