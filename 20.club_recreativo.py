basico = 0
premium = 0
familiar = 0 
total_recaudo = 0
registro = int(input("¿Cuantas personas desea registrar?: "))
for i in range (0, registro,1):
    nombre = input("Digite su nombre: ")
    edad = int(input("Digite su edad: "))
    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")
    plan = int(input("Escoja el tipo de plan:\n 1.Basico\n 2.Premium\n 3.Familia\n"))
    if plan == 1:
        basico+=1
        total_recaudo+=50000
    elif plan == 2:
        premium+=1
        total_recaudo+=90000
    elif plan == 3:
        familiar+=1
        total_recaudo+=130000
if basico > premium and basico > familiar:
    print("El plan mas vendido fue basico")
elif premium > basico and premium < familiar:
    print("El plan mas vendido fue premium")
elif familiar > basico and familiar > premium:
    print("El plan mas vendido fue familiar")
else:
    print("Mas de una plan fue vendido igual cantidad de veces")
print(f"Total recaudado es:{total_recaudo}")
print(f"Cantidad de personas por el plan basico:{basico}")
print(f"Cantidad de personas por el plan premium:{premium}")
print(f"Cantidad de personas por el plan familiar:{familiar}")