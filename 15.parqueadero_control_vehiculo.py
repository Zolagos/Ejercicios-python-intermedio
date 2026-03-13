carro = 0
moto = 0
placa_i = ""
monto = 0
total = 0
for i in range (0, 8, 1):
    placa = input("Ingrese su placa: ")
    tipo = int(input("Tipo de vehiculo:\n 1.Carro\n 2.Moto\n"))
    hora = int(input("¿Cuantas horas estuvo parqueado?:\n"))
    if tipo == 1:
        total_carro = 4000 * hora
        carro+=1
        total+=total_carro
        if total_carro > monto:
            placa_i = placa
            monto = total_carro
    elif tipo == 2:
        totalo_moto = 2000 * hora
        moto+=1
        total+=totalo_moto
        if totalo_moto > monto:
            placa_i = placa
            monto = totalo_moto
print(f"Total recaudado: {total}\n Cantidad de carros que ingresaron:{carro}\n Cantidad de motos que ingresaron:{moto}")
print(f"El vehiculo que pago mas fue: {placa_i} y pago un total de: {monto}")
