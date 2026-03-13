edad = int(input("Ingrese su edad:\n"))
if edad < 12:
    print("El valor de su entrada es de: 8000")
elif 12 <= edad <= 59:
    print("El valor de su entrada es de: 12000")
elif edad >= 60:
    print("El valor de su entrada es de: 9000")