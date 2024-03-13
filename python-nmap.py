#Importamos la herramienta de nmap que previamente hemos instalado (pip install python-nmap)

import nmap

#Declaramos un objeto con el que nos va a permitir escanear con la biblioteca de nmap

scaner = nmap.PortScanner()

#Declaramos variables a introducir por el usuario, en este caso, ip y puerto

ip_escaneo = input("Introduce la IP:")
puerto = input("Introduce el puerto:")
protocolo = input("Introduce el protocolo:")

#Con este comando, lanzamos el escaneo sobre el input ya sea fijo o variable

scaner.scan(ip_escaneo, puerto, arguments=f' -sV {protocolo}')

#Imprimo los resultados

print("¡Escaneo completado! :D")
print(f"Estado del puerto {puerto}:", scaner[ip_escaneo].state())
print(f"Protocolos escaneados {protocolo}:", scaner[ip_escaneo].all_protocols())