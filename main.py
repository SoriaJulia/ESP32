# Escribir un programa para el esp32, basado en el circuito utilizado en el capítulo 9, que publique un solo mensaje, 
# a un broker mqtt, cuando la temperatura supera un valor establecido como "temperatura superior". El sistema no volverá a publicar mensajes hasta no haber 
# estado por debajo de un límite inferior y volver a superar la temperatura superior.

from machine import Pin, Timer, unique_id
import dht
import time
import json
import ubinascii
from collections import OrderedDict
from settings import SERVIDOR_MQTT
from umqtt.robust import MQTTClient

CLIENT_ID = ubinascii.hexlify(unique_id()).decode('utf-8')

mqtt = MQTTClient(CLIENT_ID, SERVIDOR_MQTT,
                  port=8883, keepalive=10, ssl=True)

d = dht.DHT22(Pin(25))
tempMin=15
tempMax=30
canPublish=True

while True:
    try:
        d.measure()
        temperatura = d.temperature()
        humedad = d.humidity()
        datos = json.dumps(OrderedDict([
            ('temperatura',temperatura),
            ('humedad',humedad)
        ]))
        print(datos)
        if temperatura > tempMax and canPublish:
            print("publicando")
            mqtt.connect()
            mqtt.publish(f"ap/{CLIENT_ID}",datos)
            mqtt.disconnect()
            canPublish = False
        if temperatura < tempMin:
            canPublish = True    
    except OSError as e:
        print("sin sensor")
    time.sleep(5)
