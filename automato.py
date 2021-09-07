
class Automato:
    def __init__(self, automato):
        self.automato = null
        self.alfabeto = null
        self.initialState = null
        self.finalState = null
        self.transicao =  null

def checarPalavra(self, palavra):
    atualState = self.initialState
    for letra in palavra:
        for transicao in self.transicao[atualState]:
            if transicao[0] == letra:
                atualState = transicao[1]

    if atualState in self.finalState:
        print(f'A palavra foi aceita.')
        return True
    else:
        print(f'A palavra não foi aceita.')
        return False

#states
#initial
#accepting
#alphabet
#transitions