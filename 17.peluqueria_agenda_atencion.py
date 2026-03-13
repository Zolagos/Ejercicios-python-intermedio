corte = 0
cepillado = 0
tintura = 0
total = 0
for i in range (0, 7, 1):
    nombre =input("Digite su nombre:\n ")
    servicio = int(input("Servicio que solicita:\n 1.Corte\n 2.Cepillado\n 3.Tintura\n"))
    if servicio == 1:
        valor_cor = int(input("Valor cancelado:\n"))
        total+=valor_cor
        cote+=1
    elif servicio == 2:
        valor_cep =int(input("Valor cancelado:\n"))
        total+=valor_cep
        cepillado+=1
    elif servicio == 3:
        valor_tin = int(input("Valor cancelado:\n"))
        total+=valor_tin
        tintura+=1
if cote > cepillado and cote > tintura:
    print("El servicio mas solicitado fue corte")
elif cepillado > cote and cepillado < tintura:
    print("El servicio mas solicitado fue cepillado")
elif tintura > cote and tintura > cepillado:
    print("El servicio mas solicitado fue tintura")
else:
    print("Mas de una servicio fue solicitado igual veces")

print(f"Total del dia:{total}")
print(f"Cantidad de clientes que se hicieron corte:{corte}")
print(f"Cantidad de clientes que se cepillaron: {cepillado}")
print(f"Cantidad de clientes que se hicieron tintura:{tintura}")