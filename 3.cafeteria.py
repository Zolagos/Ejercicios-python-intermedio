cafe = 4000
te = 3500
jugo = 5000
bebida = int(input("¿Que bebida desea?:\n 1. Cafe\n 2. Te\n 3. Jugo\n"))
if bebida == 1:
    de = int(input("Cuantos cafes desea?: "))
    saldo = cafe * de
elif bebida == 2:
    de = int(input("Cuantos te desea?: "))
    saldo = te * de
elif bebida == 3:
    de = int(input("Cuantos jugos desea?: "))
    saldo = jugo * de
else:
    saldo=0
print(f"Su total a pagar es:{saldo}")

