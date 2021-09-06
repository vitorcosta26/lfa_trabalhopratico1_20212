from add import menu,sub_menu,encerrar


menu()

while True:
    resposta = int(input(f'1 - Imprimir autômato\n'+
                         f'2 - Transformar autômato\n'+
                         f'3 - Testar palavra\n'+
                         f'4 - Finalizar progama\n\n'))

    if resposta == 1:
        sub_menu("Imprimir autômato")

    if resposta == 2:
        sub_menu("Transformar autômato")

    if resposta == 3:
        sub_menu("Testar palavra")

    if resposta == 4:
        sub_menu("Finalizar progama")
        encerrar()
        break