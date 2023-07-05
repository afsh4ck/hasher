import hashlib

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
    texto = input("[*] Introduce el texto a hashear en SHA256S: ")
    valor_hash = hashlib.sha256(texto.encode()).hexdigest()
    print("[*] Hash:", valor_hash)
    print(divider)
    
cabecera()
while True:
    hasher()
