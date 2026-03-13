corte = 0
cepillado = 0
tintura = 0
for i in range (0, 7, 1):
    nombre =input("Digite su nombre:\n ")
    servicio = int(input("Servicio que solicita:\n 1.Corte\n 2.Cepillado\n 3.Tintura\n"))
    if servicio == 1:
        valor_cor = int(input("Valor cancelado:\n"))
        cote+=1
    elif servicio == 2:
        valor_cep =int(input("Valor cancelado:\n"))
        cepillado+=1
    elif servicio == 3:
        valor_tin = int(input("Valor cancelado:\n"))
        tintura+=1
total = valor_cor + valor_cep + valor_tin
print(f"Total del dia:{total}\n Cantidad de clientes que se hicieron corte:{corte}\n Cantidad de clientes que se cepillaron: {cepillado}\n Cantidad de clientes que se hicieron tintura:{tintura}")
#falta servicio mas solicitado 