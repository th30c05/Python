#Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
#función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
#correcta si solo tiene una “@” y si tiene uno o más “.”


mail = str(input("Mail: "))

at = 0
dot = 0
error = False

for i in mail:
    if i == "@":
        at = at + 1
    elif i == ".":
        dot = dot + 1
    elif i == " ":
        error = True

if error == True or at > 1 or at < 1 or dot < 1:
    print("Incorrect Mail")
else:
    print("Correct mail")
    