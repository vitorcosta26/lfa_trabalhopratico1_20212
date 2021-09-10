import re

class Automato:
    def __init__(self, automato, states, initial, accepting, alphabet, transitions):
        self.automato = automato
        self.states = states
        self.initial = initial
        self.accepting = accepting
        self.alphabet = alphabet
        self.transitions = transitions
        self.tipo = self.type()
    
    @staticmethod
    def ler_automato(nomeArquivo):
        automato = []
        tipo = ""

        arquivo = open(nomeArquivo+".txt", "r")
        for linha in arquivo:
            automato.append(linha.strip("\n"))
        arquivo.close()

        automato = "|".join(automato).strip()
        automato = automato.split("#")

        for i in range(len(automato)):
            if "states" in automato[i]:
                states = automato[i].split("|")
                states.remove("states")
                if "" in states:
                    states.remove("")
            if "initial" in automato[i]:
                initial = automato[i].split("|")
                initial.remove("initial")
                if "" in initial:
                    initial.remove("")
            if "accepting" in automato[i]:
                accepting = automato[i].split("|")
                accepting.remove("accepting")
                if "" in accepting:
                    accepting.remove("")
            if "alphabet" in automato[i]:
                alphabet = automato[i].split("|")
                alphabet.remove("alphabet")
                if "" in alphabet:
                    alphabet.remove("")
            if "transitions" in automato[i]:
                transitions = automato[i].split("|")
                transitions.remove("transitions")
                if "" in transitions:
                    transitions.remove("")
        
        for i in range(len(transitions)):
            transitions[i] = re.split(">|:|,", transitions[i])
        
        return Automato(automato, states, initial, accepting, alphabet, transitions)
    
    def type(self):
        tipo = ""
        if self.is_deterministic():
            tipo = "Determinístico"
        else:
            tipo = "Não-Determinístico"
        if self.is_empty_transition():
            tipo = "Não-Determinístico com Transições Vazias"
        return tipo

    def imprimir(self):
        print("Tipo\n"+self.tipo)
        print("Estados")
        for i in range(len(self.states)):
            print(self.states[i])
        print("Estado Inicial")
        for i in range(len(self.initial)):
            print(self.initial[i])
        print("Estados de Aceitação")
        for i in range(len(self.accepting)):
            print(self.accepting[i])
        print("Alfabeto")
        for i in range(len(self.alphabet)):
            print(self.alphabet[i])
        print("Transições")
        for i in range(len(self.transitions)):
            print(self.transitions[i])
        print("\n")
    
    def is_deterministic(self):
        deterministic = True
        for i in range(len(self.transitions)):
            if len(self.transitions[i]) > 3:
                deterministic = False
        return deterministic
    
    def is_empty_transition(self):
        empty_transition = False
        for i in range(len(self.transitions)):
            if "$" in self.transitions[i]:
                empty_transition = True
        return empty_transition
    
    def checarPalavra(self, palavra):
        atualState = self.initial
        for letra in palavra:
            for transicao in self.transitions[atualState]:
                if transicao[0] == letra:
                    atualState = transicao[1]

        if atualState in self.accepting:
            print(f'A palavra foi aceita.')
            return True
        else:
            print(f'A palavra não foi aceita.')
            return False
