# Encriptar / Desencriptar mensagem por transposição
# frankbexxx

import math


def main():
    # mensagem
    mensagem = 'Common sense is not so common.'

    # chave da mensagem
    k = 8

    mensagemCifrada = (cifra(k, mensagem))
    print(mensagemCifrada)
    mensagemDecifrada = (decifra(k, mensagemCifrada))
    print(mensagemDecifrada)


def cifra(key, mensagem):
    # comprimento da mensagem
    men = len(mensagem)
    # numero de linhas da mensagem a encriptar, arredondada para cima
    lin = math.ceil(men / key)
    # inicialização da string
    cripto = ''

    # ciclo que percorre a mensagem, transpondo para 'linha * chave + coluna', até ao limite do comprimento da mensagem
    for c in range(key):
        for l in range(lin):
            a = l * key + c
            if a < men:
                cripto += mensagem[a]

    return cripto


def decifra(key, mensagemCifrada):
    # comprimento da mensagem cifrada
    comprimento = len(mensagemCifrada)
    # numero de colunas da mensagem a desencriptar, arredondada para cima
    colunas = math.ceil(comprimento / key)
    # inicialização da string
    decripto = ''
    # equivalência a eliminar *********************************
    linhas = key
    # area total
    area = colunas * linhas
    # diferença entre comprimento da mensagem cifrada e o total possível
    areaInutil = area - comprimento

    for i in range(colunas):
        conta = 1
        for e in range(linhas):
            a = i + e * colunas
            if e * colunas > area - colunas * areaInutil:
                a -= conta
                conta += 1
            decripto += mensagemCifrada[a]
            if i == (colunas - 1) and e >= (linhas - areaInutil - 1):
                break
    return decripto


if __name__ == '__main__':
    main()


"""
Result: "Cenoonommstmme oo snnio. s s c"
"""