parqui = int(input("¿Cuantas horas estuvo en el parqueadero?: "))
if parqui == 1:
    print("Total a pagar: 5000")
elif parqui > 1:
    adi = 5000 + ((parqui-1)*3000)
    print(f"Total a pagar:{adi}")