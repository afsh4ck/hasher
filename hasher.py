import hashlib

verde = "\033[1;32m"
amarillo = "\033[1;33m"
magenta = "\033[95m"
cyan = "\033[96m"
default = "\033[0m"


def cabecera():
    print(title)
    print(divider)


title = """
$$\                           $$\                           
$$ |                          $$ |                          
$$$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\  \____$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ 
$$ |  $$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$  __$$ | \____$$\ $$ |  $$ |$$   ____|$$ |      
$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      
\__|  \__| \_______|\_______/ \__|  \__| \_______|\__|      

A really simple multiple encripting              < afsh4ck >
"""

divider = """------------------------------------------------------------
"""


def menu():
    print(verde + "[*] Selecciona el tipo de cifrado:" + default)
    print("1. NTLM")
    print("2. MD5")
    print("3. SHA256")
    print("4. Salir")
    opcion = input(amarillo + "[*] Escribe el número de la opción: " + default)
    return opcion


def hasher(tipo_cifrado):
    texto = input(
        magenta + "[*] Introduce el texto a cifrar en " + tipo_cifrado + ": " + default)
    if tipo_cifrado == "NTLM":
        valor_hash = hashlib.new('md4', texto.encode('utf-16le')).hexdigest()
    elif tipo_cifrado == "MD5":
        valor_hash = hashlib.md5(texto.encode()).hexdigest()
    else:
        valor_hash = hashlib.sha256(texto.encode()).hexdigest()
    print(cyan + "[*] " + tipo_cifrado + " hash:" + default, valor_hash)
    print(divider)


cabecera()
while True:
    opcion = menu()
    if opcion == "1":
        hasher("NTLM")
    elif opcion == "2":
        hasher("MD5")
    elif opcion == "3":
        hasher("SHA256")
    elif opcion == "4":
        break
    else:
        print("Opción no válida")
    respuesta = input(amarillo + "[*] ¿Deseas hacer otra operación? (S/N): ")
    if respuesta.upper() == "N":
        break
    elif respuesta.upper() == "S":
        continue

print(verde + "[*] ¡Hasta luego!")
