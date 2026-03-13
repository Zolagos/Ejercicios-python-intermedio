cafe = 4000
capuchino = 7000
pastel = 6000
op = ""
while op !=5:
    op = int(input("¿Que desea pedir?:\n 1.Cafe\n 2.Capuchino\n 3.Pastel\n 4.Siguiente cliente\n 5.Salir\n"))
    if op == 1:
        caf = int(input("¿Cuantos cafes desea?: "))
        total_caf = caf * cafe
    elif op == 2:
        cap = int(input("¿Cuantos capuchinos desea?: "))
        total_cap = cap * capuchino
    elif op == 3:
        pas = int(input("¿Cuantos pasteles desea?: "))
        total_pas = pas * pastel
    
    elif op == 5:
        print("Saliendo")
total = total_caf + total_cap + total_pas
if total > 20000: 
    total = total * 0.10
    print("")
