cono = 3000
vaso = 4000
banana_split = 9000
conn = 0
vasso = 0
banani = 0
cliente = 0
total_con = 0
total_vaso = 0
total_ban = 0
op = ""
while op !=4:
    op = int(input("Eliga una opcion:\n 1.Cono\n 2.Vaso\n 3.Banana split\n 4.salir\n"))
    if op == 1:
        con = int(input("¿Cuantos conos quiere?: "))
        precio_con = con * cono
        total_con+=precio_con
        conn+=1
        cliente+=1
    elif op == 2:
        va = int(input("¿Cuantos vasos quiere?: "))
        precio_vaso =  va * vaso
        total_vaso+=precio_vaso
        vasso+=1
        cliente+=1
    elif op == 3:
        banana = int(input("¿Cuantas bananas splits quiere?: "))
        precio_ban = banana * banana_split
        total_ban+=precio_ban
        banani+=1
        cliente+=1
    elif op == 4:
        print("Saliendo")
if conn > vasso and conn > banani:
    ven = "Cono"
elif vasso > conn and vasso > banani:
    ven = "Vaso"
elif banani > conn and banani > vasso:
    ven = "Banana Split"
else:
    ven = "Dos productos o mas se pidieron igual cantidad de veces"
    
total_ven = total_con + total_vaso + total_ban
print(f"Total vendido: {total_ven}\n Clientes atendidos:{cliente}\n Producto mas vendido: {ven}")
    