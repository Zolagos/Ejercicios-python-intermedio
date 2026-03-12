cono = 3000
vaso = 4000
banana_split = 9000
op = ""
while op !=4:
    try:
        op = int(input("Eliga una opcion:\n 1.Cono\n 2.Vaso\n 3.Banana split\n 4.salir\n"))
        if op == 1:
            con = int(input("¿Cuantos conos quiere?: "))
            total_con = con * cono
        elif op == 2:
            va = int(input("¿Cuantos vasos quiere?: "))
            total_vaso =  va * vaso
        elif op == 3:
            banana = int(input("¿Cuantas bananas splits quiere?: "))
            total_ban = banana * banana_split
        elif op == 4:
            print("Saliendo")
    except:
        print("El dato no es valido")