"""
Crea un módulo para validación de contraseñas. Dicho módulo deberá cumplir con los siguientes criterios de aceptación:

La contraseña debe contener un mínimo de 8 caracteres.
Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
La contraseña no puede contener espacios en blanco.
Contraseña válida: retorna “Contraseña ingresada correctamente”.
Contraseña no válida: retorna el mensaje "La contraseña elegida no es válida".
"""


Valida = False
espacio = " "

while Valida == False:
    contraseña = input("\nIngrese su contraseña:\n")
    if len(contraseña) < 8 or contraseña.isupper() == True or contraseña.islower() == True or contraseña.isnumeric() == True or contraseña.isalpha() == True or contraseña.isalnum() == True or espacio in contraseña:
        Valida = False
        print("La contraseña elegida no es válida")
    else:
        print("Contraseña ingresada correctamente")
        break
    
        
    
