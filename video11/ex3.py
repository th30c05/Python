stop=False

while stop==False:
    print("Dame 3 numeros y hare la media aritmetica")
    n1=int(input("Numero: "))
    n2=int(input("Otro numero: "))
    n3=int(input("Ultimo numero: "))
    print("La media aritmetica es: "+str((n1+n2+n3)/3))
    correcto=False
    while correcto==False:
        otra=input("Quieres calcular otra media aritmetica? (Si // No) ")
        if otra=="Si" or otra=="si" or otra=="sI" or otra=="SI" or otra=="S" or otra=="s":
            correcto=True;stop=False
        elif otra=="No" or otra=="no" or otra=="nO" or otra=="NO" or otra=="N" or otra=="n":
            correcto=True;stop=True
        else:
            print("Solo escribe Si o No.")
            correcto=False