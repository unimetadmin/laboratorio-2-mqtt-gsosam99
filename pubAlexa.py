import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import requests


url = "https://api.ambeedata.com/weather/latest/by-lat-lng"
querystring = {"lat":"10.491","lng":"-66.902"}
headers = {
    'x-api-key': "LAL88GSFNN2Gyv745ERJq4VywZ4l5hJg1JxY3JSo",
    'Content-type': "application/json"
    }


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

    while(cantHoras>hora):
        hora+=1
        horaBase = horaBase + datetime.timedelta(hours=1) 
        while(cantidadDeDispositivos > 0):
            
            response = requests.request("GET", url, headers=headers, params=querystring)

            d = json.loads(response.text)

            payload = {
                "fecha": str(horas),
                "Persona": "Alexa, cómo esta el clima en Caracas?",
                "Alexa": "El clima en caracas está a " + d["data"]["temperature"] + " grados"
            }

            client.publish('unimet/admin/bd',json.dumps(payload),qos=0)	

            cantidadDeDispositivos -= 1
            print(payload)
            time.sleep(0.5)
        cantidadDeDispositivos = 5


if __name__ == '__main__':
    main()
sys.exit(0)