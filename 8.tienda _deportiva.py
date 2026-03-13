pro = 0
for i in range (0, 6, 1):
    precio = int(input(f"Digite el precio del producto {i}: "))
    if precio > 100000:
        pro+=1
print(f"{pro} Cuestan mas de 100000")