hora = int(input("Digite su hora de llegada en un rango de 0 a 23:\n"))
if 6 <= hora <= 11:
    print("Horas de la mañana")
elif 12 <= hora <= 17:
    print("Horas de la tarde")
elif 18 <= hora <= 22:
    print("Horas de la noche")
else:
    print("Fuera de horario")