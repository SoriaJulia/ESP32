# Ejercicio 2
# Escribir un programa para el esp32, basado en el circuito utilizado en el capítulo 2, que detecte pulsaciones cortas y largas.
# Si se presiona el pulsador por un intervalo de 200 a 400 ms se considera como pulsación corta.
# Si en cambio se mantiene presionado por 600 ms o más se estaría en presencia de una pulsación larga.
# En ambos se deberá imprimir en consola el tipo de evento.

from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador = 0
while True:
    while sw.value():
        contador += 1
        time.sleep_ms(1)
    if 200 < contador < 400:
        print(f'Pulsación corta de {contador}ms')
    elif contador > 600:
        print(f'Pulsación larga de {contador}ms')
    contador = 0