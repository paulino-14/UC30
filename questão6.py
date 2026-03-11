idade = int(input("Digite a idade do atleta: "))


if idade < 12:
    print("Categoria: Infantil")
elif idade < 18:
    print("Categoria: Juvenil")
elif idade < 60:
    print("Categoria: Adulto")
else:
    print("Categoria: Sênior")

    print("Bem-vindo a competição de natação !")