bajo = 0
medio = 0
alto = 0
nota_global = 0
mejor_nota = 0
estudiantes = int(input("¿Cuantos estudiantes son?: "))
for i in range (0,estudiantes,1):
    nombre = input("Digite su nombre: ")
    nota_speaking = int(input("Digite su nota de speaking: "))
    nota_listening = int(input("Digite su nota de listening: "))
    nota_reading = int(input("Digite su nota de reading: "))
    nota_general = (nota_speaking+nota_listening+nota_reading)/3
    if nota_general > mejor_nota:
        mejor_nota = nota_general
        estudiantes_i = nombre
    nota_global+= nota_general
    if nota_general < 60:
        bajo+=1
    elif 60 <= nota_general <= 79:
        medio+=1
    elif nota_general >= 80:
        alto+=1
promedio = nota_global / estudiantes
print(f"El promedio general del grupo es:{promedio}")
print(f"El mejor estudiante es:{estudiantes_i} y su nota fue:{mejor_nota}")
print(f"En nivel bajo quedaron:{bajo} estudiantes")
print(f"En nivel medio quedaron:{medio} estudiantes")
print(f"En nivel alto quedaron:{alto} estudiantes")