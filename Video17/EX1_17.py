petit=False
numerito2=0
while petit == False:
    numerito=int(input("Numero: "))
    if numerito > numerito2:
        numerito2 = numerito
        petit = False
    else:
        petit = True