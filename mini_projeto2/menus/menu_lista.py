import listas as lt


def menu_lista():
    lista = []

    while True:
        print("\n   Menu")
        print("1. Criar uma lista")
        print("2. Acrescentar um elemento à lista")
        print("3. Inserir um elemento na lista")
        print("4. Remover um elemento pelo índice")
        print("5. Remover um elemento da lista")
        print("6. Ordenar a lista")
        print("7. Encontrar o valor máximo")
        print("8. Encontrar a posição do valor máximo")
        print("9. Calcular a soma dos elementos")
        print("10. Calcular a média dos elementos")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            lista = lt.cria_lista()
            print(lista)
        elif choice == "2":
            n = input("Digite o elemento a acrescentar: ")
            lista = lt.acrescenta_elemento(lista, n)
            print(lista)
        elif choice == "3":
            lt.insere_elemento(lista)
            print(lista)
        elif choice == "4":
            lt.remove_de_inice(lista)
            print(lista)
        elif choice == "5":
            lt.remove_elemento(lista)
            print(lista)
        elif choice == "6":
            lista = lt.ordena(lista)
            print(lista)
        elif choice == "7":
            max_element = lt.maximo(lista)
            print(f"O valor máximo é: {max_element}")
        elif choice == "8":
            pos_max = lt.posicao_maximo(lista)
            print(f"A posição do valor máximo é: {pos_max}")
        elif choice == "9":
            soma_total = lt.soma(lista)
            print(f"A soma dos elementos é: {soma_total}")
        elif choice == "10":
            media_valor = lt.media(lista)
            print(f"A média dos elementos é: {media_valor}")
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_lista()


