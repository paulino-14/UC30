total = 0
while True:
    valor = float(input("Digite o valor da compra (0 para parar): "))
    if valor == 0:
        break
    total += valor
print("Total das compras:", total)
