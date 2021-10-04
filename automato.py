import re
import copy

class Automato:
    def __init__(self, arquivo):
        self.automato, e, e_i, e_a, a, t, l_t = self.ler_arquivo(arquivo)
        self.estados = e
        self.estado_inicial = e_i
        self.estados_aceitacao = e_a
        self.alfabeto = a
        self.transicoes = t
        self.lista_transicoes_original = l_t

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
                lista_transicoes = automato[i].split("|")
                lista_transicoes.remove("transitions")
                if "" in lista_transicoes:
                    lista_transicoes.remove("")

        transicoes = {}

        for t in range(len(lista_transicoes)):
            lista_transicoes[t] = re.split(">|:|,", lista_transicoes[t])
            transicoes[(lista_transicoes[t][0], lista_transicoes[t][1])] = lista_transicoes[t][2:]

        lista_transicoes

        return automato, estados, estado_inicial, estados_aceitacao, alfabeto, transicoes, lista_transicoes

    def imprimir(self):
        print("#states")
        for e in self.estados:
            print(e)
        print("#initial")
        for e_i in self.estado_inicial:
            print(e_i)
        print("#accepting")
        for e_a in self.estados_aceitacao:
            print(e_a)
        print("#alphabet")
        for s in self.alfabeto:
            print(s)
        print("#transitions")
        for t in self.transicoes:
            print(f"{t[0]}:{t[1]}>", end="")
            for i, e in enumerate(self.transicoes[t]):
                print(f"{e}", end="")
                if i != len(self.transicoes[t]) - 1:
                    print(",", end="")
                else:
                    print()

    def tipo(self):
        if self.determinístico_():
            tipo = "Determinístico"
        else:
            tipo = "Não-Determinístico"
        if self.transicoes_vazias_():
            tipo = "Não-Determinístico com Transições Vazias"

        return tipo

    def determinístico_(self):
        determinístico = True

        for transicao in self.transicoes:
            if len(self.transicoes[transicao]) > 1:
                determinístico = False

        return determinístico

    def transicoes_vazias_(self):
        transicoes_vazias = False

        for transicao in self.transicoes:
            if "$" in transicao:
                transicoes_vazias = True

        return transicoes_vazias

    def converter(self):
        subconjuntos = []
        estados_condicoes = {}

        estados_dfa = []
        estados_aceitacao_dfa = []

        for estado in self.estados:
            subconjuntos.append([estado])
            for estado_ in self.estados:
                if estado != estado_:
                    novo_estado = sorted([estado, estado_])
                    if novo_estado not in subconjuntos:
                        subconjuntos.append(novo_estado)

        subconjuntos.append(self.estados)

        transicoes_dfa = {}
        for transicao in self.lista_transicoes_original:
            for estado in subconjuntos:
                for simbolo in self.alfabeto:
                    for estado_ in estado:
                        if estado_ == transicao[0] and simbolo == transicao[1]:
                            estado_condicao = (''.join(estado), simbolo)
                            if estado_condicao in estados_condicoes.keys():
                                estado_aceitacao = estados_condicoes[estado_condicao]
                                estado_aceitacao.append("".join(transicao[2:]))
                                estados_condicoes[estado_condicao] = estado_aceitacao
                            else:
                                estados_condicoes[estado_condicao] = transicao[2:]

        estados_busca = copy.deepcopy(self.estado_inicial)
        estados_visitados = []
        while estados_busca:
            for estado_ in estados_busca:
                estado = estado_

            estados_visitados.append(estado)

            for t in sorted(estados_condicoes):
                if estado in t[0]:
                    if ''.join(estados_condicoes[t]) not in estados_busca and ''.join(
                            estados_condicoes[t]) not in estados_visitados:
                        estados_busca.append(''.join(estados_condicoes[t]))
            estados_busca.remove(estado)

        for estado in estados_visitados:
            for t in sorted(estados_condicoes):
                if estado in t:
                    transicoes_dfa[t] = [''.join(estados_condicoes[t])]
                    for e_a in self.estados_aceitacao:
                        if e_a in estados_condicoes[t] and e_a not in estados_aceitacao_dfa:
                            estados_aceitacao_dfa.append(''.join(estados_condicoes[t]))

        for estado in transicoes_dfa.items():
            if estado[0][0] not in estados_dfa:
                estados_dfa.append(estado[0][0])

        self.transicoes = copy.deepcopy(transicoes_dfa)
        self.estados = copy.deepcopy(estados_dfa)
        self.estados_aceitacao = copy.deepcopy(estados_aceitacao_dfa)

    def testar_palavra(self, palavra):
        if self.tipo() == "Não-Determinístico":
            self.converter()

        for estado in self.estado_inicial:
            estado_atual = estado

        for letra in palavra:
            if letra not in self.alfabeto:
                print(f"A palavra {palavra} não pode ser testada, pois seus símbolos não fazem parte do alfabeto definido.")
                return False

        for letra in palavra:
            estado_atual = ''.join(self.transicoes[(estado_atual, letra)])

        if estado_atual in self.estados_aceitacao:
            print(f'A palavra {palavra} foi aceita.')
            return True
        else:
            print(f'A palavra {palavra} foi rejeitada.')
            return False

    def testar_palavra_transicao_vazia(self, palavra = ""):
        for estado in self.estado_inicial:
            estado_atual = estado

        for letra in palavra:
            if letra != "":
                if letra not in self.alfabeto:
                    print(f"A palavra {palavra} não pode ser testada, pois seus símbolos não fazem parte do alfabeto definido.")
                    return False

        if len(palavra) == 0:
            estado_atual = ''.join(self.transicoes[(estado_atual, "$")])
        elif len(palavra) == 1:
            if palavra.isnumeric():
                for i, letra in enumerate(palavra):
                    if int(letra) > 0 and i == 0:
                        estado_atual = ''.join(self.transicoes[(estado_atual, "+")])
                        letra_ = letra
                estado_atual = ''.join(self.transicoes[(estado_atual, letra_)])
            else:
                for letra in palavra:
                    estado_atual = ''.join(self.transicoes[(estado_atual, letra)])
        else:
            if palavra.isnumeric():
                for i, letra in enumerate(palavra):
                    if int(letra) > 0 and i == 0:
                        estado_atual = ''.join(self.transicoes[(estado_atual, "+")])
                        letra_ = letra
                    elif i > 0:
                        letra_ = letra
                estado_atual = ''.join(self.transicoes[(estado_atual, letra_)])
            else:
                for letra in palavra:
                    estado_atual = ''.join(self.transicoes[(estado_atual, letra)])

        if estado_atual in self.estados_aceitacao:
            print(f'A palavra {palavra} foi aceita.')
            return True
        else:
            print(f'A palavra {palavra} foi rejeitada.')
            return False
