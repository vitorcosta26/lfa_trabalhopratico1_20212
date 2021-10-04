import re

class Automato:
    def __init__(self, arquivo):
        self.automato, e, e_i, e_a, a, t = self.ler_arquivo(arquivo)
        self.estados = e
        self.estado_inicial = e_i
        self.estados_aceitacao = e_a
        self.alfabeto = a
        self.transicoes = t
        self.tipo = self.tipo()
    
    @staticmethod
    def ler_arquivo(nomeArquivo):
        automato = []

        arquivo = open(nomeArquivo + ".txt", "r")
        for linha in arquivo:
            automato.append(linha.strip("\n"))
        arquivo.close()

        automato = "|".join(automato).strip()
        automato = automato.split("#")

        for i in range(len(automato)):
            if "states" in automato[i]:
                estados = automato[i].split("|")
                estados.remove("states")
                if "" in estados:
                    estados.remove("")
            if "initial" in automato[i]:
                estado_inicial = automato[i].split("|")
                estado_inicial.remove("initial")
                if "" in estado_inicial:
                    estado_inicial.remove("")
            if "accepting" in automato[i]:
                estados_aceitacao = automato[i].split("|")
                estados_aceitacao.remove("accepting")
                if "" in estados_aceitacao:
                    estados_aceitacao.remove("")
            if "alphabet" in automato[i]:
                alfabeto = automato[i].split("|")
                alfabeto.remove("alphabet")
                if "" in alfabeto:
                    alfabeto.remove("")
            if "transitions" in automato[i]:
                transicoes = automato[i].split("|")
                transicoes.remove("transitions")
                if "" in transicoes:
                    transicoes.remove("")

        for i in range(len(transicoes)):
            transicoes[i] = re.split(">|:|,", transicoes[i])

        return automato, estados, estado_inicial, estados_aceitacao, alfabeto, transicoes
    
    def tipo(self):
        if self.determinístico_():
            tipo = "Determinístico"
        else:
            tipo = "Não-Determinístico"
        if self.transicoes_vazias_():
            tipo = "Não-Determinístico com Transições Vazias"
            
        return tipo

    def imprimir(self):
        print("Tipo\n"+self.tipo)
        print("Estados")
        for e in self.estados:
            print(e)
        print("Estado Inicial")
        for e_i in self.estado_inicial:
            print(e_i)
        print("Estados de Aceitação")
        for e_a in self.estados_aceitacao:
            print(e_a)
        print("Alfabeto")
        for s in self.alfabeto:
            print(s)
        print("Transições")
        for t in self.transicoes:
            print(f"{t[0]}:{t[1]}>{''.join(t[2:])}")
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
