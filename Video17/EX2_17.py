#Crea un programa que pida números positivos indefinidamente. 
#El programa termina cuando se introduce un número negativo. 
# Finalmente el programa muestras la suma de todos los números introducidos.

suma = 0
negativo = False

while negativo == False:
    numero = int(input ("Numero: "))
    if numero < 0:
        print("Error Numero Negativo")
        negativo = True
        print("Suma total de "+str(suma))
    else:
        suma = suma + numero
        negativo = False
        