import hashlib

def cabecera():
    print(title)
    print(name)
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

"""

name = """Developed by: afsh4ck
"""

divider = """----------------------------------------------------------
"""


def hasher():
    cabecera()
    cadena = input("Introduce el texto a hashear en SHA256S: ")
    valor_hash = hashlib.sha256(cadena.encode()).hexdigest()
    print("Hash:", valor_hash)
    return

hasher()
