from add import menu,sub_menu,encerrar

menu()

while True:
    resposta = int(input(f'1 - Cadastrar autômato\n'+
                        f'2 - Imprimir autômato\n'+
                        f'3 - Transformar autômato\n'+
                        f'4 - Testar palavra\n'+
                        f'0 - Finalizar progama\n\n'))
    
    if resposta == 1:
        sub_menu("Cadastrar autômato")
        nome = input("Digite o nome do arquivo, sem o\".txt.\": ")
        automato = Automato.ler_automato(nome)

    elif resposta == 2:
        sub_menu("Imprimir autômato")
        Automato.imprimir(automato)

    elif resposta == 3:
        sub_menu("Transformar autômato")

    elif resposta == 4:
        sub_menu("Testar palavra")

    elif resposta ==0:
        sub_menu("Finalizar progama")
        encerrar()
        break