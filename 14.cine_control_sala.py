niño = 0
adulto = 0
adulto_mayor = 0
sala = int(input("Capacidad total de la sala de cine:\n"))
cantidad = int(input("¿Cuantas personas van a ingresar a la sala?:\n"))
for i in range ( 0, cantidad, 1):
    edad = int(input("Digite su edad: "))
    if edad <= 12:
        niño+=1
    elif 13 <= edad <=29:
        adulto+=1
    elif edad >= 30:
        adulto_mayor+=1
if cantidad < sala:
    print("No se lleno la sala de cine")
else:
    print("Se lleno la sala de cine")
print(f"Total de personas ingresadas:{cantidad}")
print(f"Total de niños:{niño}")
print(f"Total de adultos:{adulto}")
print(f"Total de adultos mayores:{adulto_mayor}")