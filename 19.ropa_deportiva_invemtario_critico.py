agotado = 0 
stock_bajo = 0
stock_normal = 0
for i in range (0, 10, 1):
    nombre = input("Digite el nombre del producto:\n")
    cantidad = int(input("Digite la cantidad solicitada: "))
    if cantidad == 0:
        agotado+=1
    elif 1 <= cantidad <=5:
        stock_bajo+=1
    elif cantidad >= 6:
        stock_normal+=1
print(f"{agotado} Productos estan agotados.")
print(f"{stock_bajo} Productos tienen stock bajo.")
print(f"{stock_normal} Productos tienen stock normal.") 