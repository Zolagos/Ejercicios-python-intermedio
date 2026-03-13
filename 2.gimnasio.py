edad = int(input("Digite su edad: "))
if 0 < edad < 13:
    print("No puede ingresar al gimnasio")
elif 13 <= edad <= 17:
    print("Clase juvenil")
elif 18 <= edad <= 59:
    print("Clase general")
elif edad >= 60:
    print("Clase senior")