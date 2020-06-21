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
