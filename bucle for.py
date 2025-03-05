for i in "fra":
    print("Hola", end=" ")

miEmail=input("Introduce email")
email=False
for i in miEmail:
    if i == "@":
        email = True
if email:
    print("El email es correcto")
else:
    print("EL mail no es correcto")



for i in range(5,10,1):
    print(f"Valor de la variable {i}")


for i in range(5,10):
    print(f"Valor de la variable {i}")

for x in "banana":
    print(x)