# Ejercicio 1
# Escribir un programa para el esp32, basado en el circuito utilizado en el capítulo 2,
# que alterne el estado del led luego de 10 pulsaciones.

from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador = 0
while True:
    if sw.value():
        contador += 1
        print(contador)
        if contador == 10:
            led.value(not led.value())
            contador = 0
    time.sleep_ms(200)