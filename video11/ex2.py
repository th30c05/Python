correcto=False
nombre=input("Nombre: ") 
direcion=input("Direccion: ")

while correcto==False:
    tfno=int(input("Telefono: "))
    if tfno<=999999999 and tfno>=100000000:
        correcto=True
    else:
        print("Escriba un numero de telefono correcto. (Ejemplo 652694664)")
        
datospersonales={"Nombre":nombre,"Direccion":direcion,"Telefono":str(tfno)}
print("Los datos personales son: "+str(datospersonales))