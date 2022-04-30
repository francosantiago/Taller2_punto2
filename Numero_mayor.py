"""PROGRAMA
PARA SABER CUAL ES EL NÙMERO MAYOR"""

print("---------------------------------")
print("--------Nùmero Mayor-------------")
print("---------------------------------")


x = int(input("Ingrese el primer nùmero: "))
y = int(input("Ingrese el segundo nùmero: "))
z = int(input("Ingrese el tercer nùmero: "))


if x > y and x > z:
    print("EL nùmero mayor es: " + str(x))
elif y > x and y > z:
    print("El nùmero mayor es: " + str(y))
elif z > x and z > y:
    print("El nùmero mayor es: " + str(z))
else:
    print("No hay nùmero mayor")