import hashlib

verde = "\033[1;32m"
amarillo = "\033[1;33m"
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

                                   < Developed by: afsh4ck >
"""

divider = """----------------------------------------------------------
"""

def hasher():
    texto = input(amarillo + "[*] Introduce el texto a hashear en SHA256S: " + default)
    valor_hash = hashlib.sha256(texto.encode()).hexdigest()
    print( verde + "[*] Hash:" + default, valor_hash )
    print(divider)
    
cabecera()
while True:
    hasher()
