helado_vainilla = 0
helado_chocolate = 0
helado_fresa = 0
op = ""
for i in range (0, 5, 1):
    op = int(input("\n¿Que sabor de helado desea?\n 1.Vinilla\n 2.Chocolate\n 3.Fresa\n"))
    if op == 1:
        helado_vainilla = helado_vainilla + 1
    elif op == 2:
        helado_chocolate = helado_chocolate + 1
    elif op == 3:
        helado_fresa = helado_fresa + 1
print(f"\nCantidad de helados de vainilla: {helado_vainilla}\n Cantidad de helados de chocolate: {helado_chocolate}\n Cantidad de helados de fresa: {helado_fresa} ")