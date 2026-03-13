bajo_comp = 0
compro_medio = 0
compro_alto =0
for i in range (0, 5, 1):
    nombre = input("Digite su nombre: ")
    asis = int(input("Dias asistidos al gym en la semana: "))
    minu = int(input("Minutos en promedio entrenado por dia: "))
    if asis < 3:
        bajo_comp+=1
    elif 3 <= asis <= 4:
        compro_medio+=1
    elif asis >= 5:
        compro_alto+=1
print(f"Cantidad de personas con bajo compromiso con el gym: {bajo_comp}\n Cantidad de personas con compromiso medio con el gym: {compro_medio}\n Cantidad de personas con compromiso alto con el gym: {compro_alto}")
