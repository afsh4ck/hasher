import os
import hashlib

verde = "\033[1;32m"
amarillo = "\033[1;33m"
magenta = "\033[95m"
cyan = "\033[96m"
default = "\033[0m"

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")  # Clear terminal

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
    print("2. MD1")
    print("3. MD2")
    print("4. MD4")
    print("5. MD5")
    print("6. SHA-1")
    print("7. SHA-224")
    print("8. SHA-256")
    print("9. SHA-384")
    print("10. SHA-512")
    print("11. RIPEMD-160")
    print("12. BLAKE2b")
    print("13. BLAKE2s")
    print("14. Salir")
    opcion = input(amarillo + "[*] Escribe el número de la opción: " + default)
    return opcion

def hasher(tipo_cifrado):
    texto = input(magenta + "[*] Introduce el texto a cifrar en " + tipo_cifrado + ": " + default)
    if tipo_cifrado == "NTLM":
        valor_hash = hashlib.new('md4', texto.encode('utf-16le')).hexdigest()
    elif tipo_cifrado == "MD1":
        valor_hash = hashlib.new('mdc2', texto.encode()).hexdigest()  # MD1 no es seguro, MDC2 se usa solo como ejemplo
    elif tipo_cifrado == "MD2":
        valor_hash = hashlib.new('md2', texto.encode()).hexdigest()
    elif tipo_cifrado == "MD4":
        valor_hash = hashlib.new('md4', texto.encode()).hexdigest()
    elif tipo_cifrado == "MD5":
        valor_hash = hashlib.md5(texto.encode()).hexdigest()
    elif tipo_cifrado == "SHA-1":
        valor_hash = hashlib.sha1(texto.encode()).hexdigest()
    elif tipo_cifrado == "SHA-224":
        valor_hash = hashlib.sha224(texto.encode()).hexdigest()
    elif tipo_cifrado == "SHA-256":
        valor_hash = hashlib.sha256(texto.encode()).hexdigest()
    elif tipo_cifrado == "SHA-384":
        valor_hash = hashlib.sha384(texto.encode()).hexdigest()
    elif tipo_cifrado == "SHA-512":
        valor_hash = hashlib.sha512(texto.encode()).hexdigest()
    elif tipo_cifrado == "RIPEMD-160":
        valor_hash = hashlib.new('ripemd160', texto.encode()).hexdigest()
    elif tipo_cifrado == "BLAKE2b":
        valor_hash = hashlib.blake2b(texto.encode()).hexdigest()
    elif tipo_cifrado == "BLAKE2s":
        valor_hash = hashlib.blake2s(texto.encode()).hexdigest()
    else:
        print("Algoritmo de hash no reconocido")
        return

    print(cyan + "[*] " + tipo_cifrado + " hash:" + default, valor_hash)
    print(divider)

cabecera()
while True:
    clear_terminal()
    cabecera()
    opcion = menu()
    if opcion == "14":
        break
    elif opcion in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:
        hasher(["NTLM", "MD1", "MD2", "MD4", "MD5", "SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512", "RIPEMD-160", "BLAKE2b", "BLAKE2s"][int(opcion) - 1])
    else:
        print("Opción no válida")
    respuesta = input(amarillo + "[*] ¿Deseas hacer otra operación? (S/N): " + default)
    if respuesta.upper() == "N":
        break
    elif respuesta.upper() == "S":
        continue

print(verde + "[*] ¡Hasta luego!")
