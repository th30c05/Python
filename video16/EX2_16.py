#Crea un programa que pida por teclado introducir una contraseña. 
#La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco. 
#Si la contraseña es correcta, el programa imprime “Contraseña OK”.
#En caso contrario imprime “Contraseña errónea”

password = str(input("Password: "))
correct = True
counter = 0

for passw in password:
    if passw == " ":
        correct =False
    else:
        counter = counter + 1

if counter >= 8 and correct == True:
    print("Password OK")
else:
    print("Password NO ok")
