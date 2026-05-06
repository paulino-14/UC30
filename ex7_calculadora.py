while True:
    print("Menu da Calculadora")
    print("1 - Soma")
    print("2 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado da soma:", n1 + n2)
    elif opcao == 2:
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")
