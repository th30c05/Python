def devuelvemax(a, b):
    if a==b:
        return print("Los numeros son iguales")
    elif a>b:
        return print("El numero "+str(a)+" es mas grande que el "+str(b)+".")
    else:
        return print("El numero "+str(b)+" es mas grande que el "+str(a)+".")

numero1=int(input("Dime un numero: "))
numero2=int(input("Dime otro numero: "))

devuelvemax(numero1, numero2)