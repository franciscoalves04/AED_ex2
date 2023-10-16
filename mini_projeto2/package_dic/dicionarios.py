def cria_dicionario():
    entrada = input("Diz um dicionario (ex:banana : 3, laranga: 7):")

    pares = entrada.split(',')
    dicionario = {}

    for par in pares:
        key, value = par.strip().split(':')
        dicionario[key.strip()] = value.strip()

    return dicionario


def insere_elemento(dicionario):
    key = input("Digite a chave: ")
    value = input("Digite o valor: ")
    dicionario[key] = value

    return dicionario

def remove_elemento(dicionario):
    key = input("Diz a chave do elemento que queres remover: ")
    if key in dicionario:
        del dicionario[key]
    else:
        print("Chave nao encontrada")

    return dicionario


def apresenta_ordenado(dicionario):
    resultado_formatado = ""
    for chave in sorted(dicionario.keys()):
        resultado_formatado += f"{chave}: {dicionario[chave]}\n"
    return resultado_formatado


def soma_valores(dicionario):
    try:
        valores = [float(valor) for valor in dicionario.values()]
        soma = sum(valores)
        return soma
    except ValueError:
        pass



def media_valores(dicionario):
    try:
        valores = [float(valor) for valor in dicionario.values()]
        soma = sum(valores)
        media = soma / len(valores)
        return media
    except ValueError:
        pass

    return media

def maximo_valor(dicionario):
    chave_max = None
    valor_max = None

    for chave, valor in dicionario.items():
        if valor_max is None or valor > valor_max:
            chave_max = chave
            valor_max = valor

    return chave_max,valor_max



