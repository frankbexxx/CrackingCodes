# Cifrador
# frankbexxx, based on Al Sweigart book
import cifraTransposicaoEncriptaDesencripta as Cted

choice = True


def cif():
    """
    funcao que pede ao utilizador uma mensagem para cifrar e grava a mensagem cifrada num ficheiro de texto
    """
    print(
        "Olá, vamos então introduzir a mensagem a cifrar, a respectiva chave, e o nome do ficheiro com a mensagem cifrada!\n"
    )
    # mensagem
    mensagem = input("Qual a mensagem que pretende cifrar? ")
    # metade do comprimento da mensagem, arredondada por defeito, para cumprir a regra máxima da chave
    metade = int(len(mensagem) // 2)
    # chave
    chave = int(
        input(
            "Qual chave pretendida? (tem que ser um número inteiro compreendido entre 1 e {}) ".format(
                metade
            )
        )
    )
    # cifra a mensagem chamando a função 'cifra'
    mensagemCifrada = Cted.cifra(chave, mensagem)
    # nome do ficheiro
    nomeFicheiro = input("Qual o nome do ficheiro? ") + ".txt"

    # grava a mensagem cifrada num ficheiro de texto
    f = open(nomeFicheiro, "w")
    for x in mensagemCifrada:
        f.write(x)
    f.close()
    return


def decif():
    """
    funcao que pede ao utilizador o nome do ficheiro com a mensagem para decifrar
    """
    print(
        "Olá, por favor introduza o nome do ficheiro a decifrar e a respectiva chave!\n"
    )
    # mensagem
    nomeFicheiro = input("Qual o nome do ficheiro? ") + ".txt"
    # chave
    chave = int(input("Qual chave para decifrar? "))
    # inicialização
    mensagemCifrada = ""

    # lê a mensagem cifrada, a partir de um ficheiro de texto
    f = open(nomeFicheiro, "r")
    for x in f:
        mensagemCifrada += x
    f.close()

    # decifra a mensagem chamando a função 'decifra'
    mensagemDecifrada = Cted.decifra(chave, mensagemCifrada)

    print("A mensagem original era: {}".format(mensagemDecifrada))

    return


while choice:
    escolha = input("Escolha uma opção, (c)ifra, (d)ecifra ou (q)uit: ")
    if escolha.lower() == "c":
        cif()
    elif escolha.lower() == "d":
        decif()
    elif escolha.lower() == "q":
        choice = False
    else:
        print("You are very dumb or blind. Please chose a valid option.\n")

# mensagemDecifrada = Cted.decifra(chave, mensagemCifrada)

# print(mensagemDecifrada)
