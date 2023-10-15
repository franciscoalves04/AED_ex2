def cria_lista():
    lista = []
    frase = input("Diz a lista separada por espaços")
    elemento = frase.split()
    for i in elemento:
        lista.append(i)
    return lista


def acrescenta_elemento(lista, n):
    lista.append(n)
    return lista

def insere_elemento(lista):
    print("Lista: ", lista)

    try:
        posicao = int(input("Onde quer inserir o elemento: "))
        valor = input("Qual o valor do elemento: ")
        lista.insert(posicao,valor)

    except IndexError:
        print("Posição fora da lista")

    except ValueError:
        print("Posição deve ser um numero inteiro")

def remove_de_inice(lista):
    print("Lista: ", lista)
    try :
        posicao = int(input("Onde quer remover o elemento: "))
        if 0 <= posicao < len(lista):
            elemt_remove = lista.pop(posicao)
            return lista

        else:
            print("Posição fora da lista")

    except ValueError:
        print("Posição deve ser um numero inteiro")


def remove_elemento(lista):
    print("Lista: ", lista)

    elemento = input("Que elemento quer remover: ")

    if elemento in lista:
        lista.remove(elemento)

    else:
        print(f"Elemento: {elemento} nao existe na lista")
    return lista



def ordena(lista):
    while True:
        ordem = input("Quer ordenar a lista em ordem crescente ou decrescente?: ").lower()

        if ordem == "crescente":
            lista.sort()
            return lista
        elif ordem == "decrescente":
            lista.sort(reverse=True)
            return lista
        else:
            print("Opção inválida. Escolha (crescente/decrescente)? ")


def maximo(lista):
    max_element = lista[0]
    for elemento in lista:
        if elemento > max_element:
            max_element = elemento
    return max_element


def posicao_maximo(lista):
    max_element = lista[0]
    pos_max = 0

    for i, elemento in enumerate(lista):
        if elemento > max_element:
            max_element = elemento
            pos_max = i
    return pos_max

def soma(lista):
    soma_total = 0
    for elemento in lista:
        try:
            soma_total += float(elemento)
        except ValueError:
            pass
    return soma_total



def media(lista):
    soma_total = 0
    for elemento in lista:
        try:
            soma_total += float(elemento)
        except ValueError:
            pass

    media = soma_total / len(lista)
    return media





