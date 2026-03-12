# Pide la cantidad de clases asistidas por un estudiante en un mes
cla = int(input("cantidad de clase asistidas en el mes: "))
if cla < 5:
    print("Asistencia baja")
elif 5 <= cla <= 8:
    print("Asistencia media")
else:
    print("Asistencia alta")