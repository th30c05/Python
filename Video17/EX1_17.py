#Crea un programa que pida números infinitamente. 
# Los números introducidos deben ser cada vez mayores.
# El programa finalizará cuando se introduce un número menor que el anterior.

petit=False
numerito2=0

while petit == False:
    numerito=int(input("Numero: "))
    if numerito > numerito2:
        numerito2 = numerito
        petit = False
    else:
        petit = True
        