from time import sleep

from add import *
from automato import Automato

menu()

while True:
    resposta = int(input('\n1 - Cadastrar autômato\n' +
                         '2 - Imprimir autômato\n' +
                         '3 - Testar palavra\n' +
                         '0 - Finalizar progama\n\nOpção: '))
    if 0 <= resposta <= 3:
        if resposta == 1:
            sub_menu("Cadastrar autômato")
            nome = input("Digite o nome do arquivo, sem o \".txt\": ")
            automato = Automato(nome)

        elif resposta == 2:
            sub_menu("Imprimir autômato")
            print("Autômato " + automato.tipo())
            automato.imprimir()
            if automato.tipo() == "Não-Determinístico":
                sleep(1)
                print("\nTransformando\n")
                sleep(1)
                automato.converter()
                print("Autômato " + automato.tipo())
                automato.imprimir()

        elif resposta == 3:
            sub_menu("Testar palavra")
            palavra = input("Digite a palavra: ")
            print()
            if automato.tipo() == "Não-Determinístico com Transições Vazias":
                automato.testar_palavra_transicao_vazia(palavra)
            else:
                automato.testar_palavra(palavra)

        else:
            sub_menu("Finalizar progama")
            encerrar()
            break
    else:
        print("Opção inválida, por favor, digite novamente!")
