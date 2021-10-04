from add import menu,sub_menu,encerrar
from automato import Automato

menu()

while True:
    resposta = int(input('\n1 - Cadastrar autômato\n' +
                         '2 - Testar palavra\n' +
                         '0 - Finalizar progama\n\nOpção: '))
    if 0 <= resposta <= 2:
        if resposta == 1:
            sub_menu("Cadastrar autômato")
            nome = input("Digite o nome do arquivo, sem o\".txt\": ")
            automato = Automato(nome)

        elif resposta == 2:
            sub_menu("Testar palavra")
            palavra = input("Digite a palavra: ")
            print()
            automato.testar_palavra(palavra)

        else:
            sub_menu("Finalizar progama")
            encerrar()
            break
    else:
        print("Opção inválida, por favor, tente novamente!")