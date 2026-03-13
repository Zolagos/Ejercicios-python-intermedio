alimento = 0
juguete = 0
accesorio = 0
total_ali = 0
total_jug = 0
total_acce = 0
for i in range (0, 10, 1):
    categoria = int(input("¿Que desea comprar:\n 1.Alimento\n 2.Juguete\n 3.Accesorio\n"))
    if categoria == 1:
        valor_ali = int(input("Digite el valor de la compra:\n"))
        total_ali+= valor_ali
        alimento+=1
    elif categoria == 2:
        valor_jug = int(input("Digite el valor de la compra:\n"))
        total_jug+= valor_jug
        juguete+=1
    elif categoria == 3:
        valor_acce = int(input("Digite el valor de la compra:\n"))
        total_acce+= valor_acce
        accesorio+=1
if total_ali > total_jug and total_ali > total_acce:
    print("La categoria que genero mas dinero fue los alimentos")
elif total_jug > total_ali and total_jug < total_acce:
    print("La categoria que genero mas dinero fue los juguetes")
elif total_acce > total_ali and total_acce > total_jug:
    print("La categoria que genero mas dinero fue los accesorios")
else:
    print("Mas de una categoria genero igual cantidad de dinero")
print(f"Se vendio un total de {alimento} en alimentos")
print(f"Se vendio un total de {juguete} en juguetes")
print(f"Se vendio un total de {accesorio} en accesorios")
