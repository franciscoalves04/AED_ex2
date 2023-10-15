import dicionarios as dc

def menu_dicionario():
    dicionario = {}

    while True:
        print("\n     Menu")
        print("1. Criar um dicionário")
        print("2. Inserir um elemento no dicionário")
        print("3. Remover um elemento do dicionário")
        print("4. Apresentar o dicionário ordenado")
        print("5. Calcular a soma dos valores")
        print("6. Calcular a média dos valores")
        print("7. Encontrar o valor máximo")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            dicionario = dc.cria_dicionario()
            print(dicionario)
        elif choice == "2":
            dc.insere_elemento(dicionario)
            print(dicionario)
        elif choice == "3":
            dc.remove_elemento(dicionario)
            print(dicionario)
        elif choice == "4":
            valores_ordenados = dc.apresenta_ordenado(dicionario)
            print(valores_ordenados)
        elif choice == "5":
            soma_total = dc.soma_valores(dicionario)
            print(f"A soma dos valores é: {soma_total}")
        elif choice == "6":
            media_valor = dc.media_valores(dicionario)
            print(f"A média dos valores é: {media_valor}")
        elif choice == "7":
            chave_max, valor_max = dc.maximo_valor(dicionario)
            print(f"O valor máximo é: {valor_max} (Chave: {chave_max})")
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


menu_dicionario()