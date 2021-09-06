from time import sleep

def menu():
    return print(f'{"x"*56}\n'+
      f'{"-"*25} MENU {"-"*25}\n'+
      f'{"x"*56}')


def sub_menu(palavra):
    return print(f'{"‹"*5} {palavra} {"›"*5}')

def encerrar():
    print('Encerrando em 3...')
    sleep(1)
    print('Encerrando em 2...')
    sleep(1)
    print('Encerrando em 1...')
    sleep(1)
    print('boom :)')