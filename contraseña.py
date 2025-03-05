import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

longitud = int(input("Longitud de la contraseña: "))
print("Contraseña generada:", generar_contraseña(longitud))
