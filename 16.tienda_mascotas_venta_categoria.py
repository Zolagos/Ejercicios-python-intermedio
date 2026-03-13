alimento = 0
juguete = 0
accesorio = 0
for i in range (0, 10, 1):
    categoria = int(input("¿Que desea comprar:\n 1.Alimento\n 2.Juguete\n 3.Accesorio\n"))
    if categoria == 1:
        valor_ali = int(input("Digite el valor de la compra:\n"))
        alimento+=1
    elif categoria == 2:
        valor_jug = int(input("Digite el valor de la compra:\n"))
        juguete+=1
    elif categoria == 3:
        valor_acce = int(input("Digite el valor de la compra:\n"))
        accesorio+=1
print(f"Se vendio un total de {alimento} en alimentos\n Se vendio un total de {juguete} en juguetes\n Se vendio un total de {accesorio} en accesorios")
