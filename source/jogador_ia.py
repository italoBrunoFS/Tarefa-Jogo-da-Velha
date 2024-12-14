# -*- coding: utf-8 -*-
from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)
        self.matriz = tabuleiro.matriz

    def getJogada(self) -> (int, int):
        # REGRA 1:
        # Verificar linhas:
        for l in range(3):
            linha = self.matriz[l]
            soma = sum(linha)
            if soma == 8 or soma == 2:
                for c in range(3):
                    if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        return (l, c)

        # Verificar colunas:
        for c in range(3):
            coluna = [self.matriz[l][c] for l in range(3)]
            soma = sum(coluna)
            if soma == 8 or soma == 2:
                for l in range(3):
                    if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                        return (l, c)

        # Verificar diagonal principal:
        diagonal_principal = [self.matriz[l][l] for l in range(3)]
        soma_diag_principal = sum(diagonal_principal)
        if soma_diag_principal == 8 or soma_diag_principal == 2:
            for l in range(3):
                if self.matriz[l][l] == Tabuleiro.DESCONHECIDO:
                    return (l, l)

        # Verificar diagonal secundária:
        diagonal_secundaria = [self.matriz[l][2 - l] for l in range(3)]
        soma_diag_secundaria = sum(diagonal_secundaria)
        if soma_diag_secundaria == 8 or soma_diag_secundaria == 2:
            for l in range(3):
                if self.matriz[l][2 - l] == Tabuleiro.DESCONHECIDO:
                    return (l, 2 - l)

        # REGRA 2: Criar duas sequências de duas marcações
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Simula a jogada
                    self.matriz[l][c] = self.tipo

                    # Verifica quantas sequências de duas marcações são criadas
                    duas_sequencias = 0

                    # Verificar linhas, colunas e diagonais
                    for linha in range(3):
                        if sum(self.matriz[linha]) == 2 * self.tipo and self.matriz[linha].count(Tabuleiro.DESCONHECIDO) == 1:
                            duas_sequencias += 1
                    for coluna in range(3):
                        coluna_atual = [self.matriz[linha][coluna] for linha in range(3)]
                        if sum(coluna_atual) == 2 * self.tipo and coluna_atual.count(Tabuleiro.DESCONHECIDO) == 1:
                            duas_sequencias += 1
                    diagonal_principal = [self.matriz[i][i] for i in range(3)]
                    if sum(diagonal_principal) == 2 * self.tipo and diagonal_principal.count(Tabuleiro.DESCONHECIDO) == 1:
                        duas_sequencias += 1
                    diagonal_secundaria = [self.matriz[i][2 - i] for i in range(3)]
                    if sum(diagonal_secundaria) == 2 * self.tipo and diagonal_secundaria.count(Tabuleiro.DESCONHECIDO) == 1:
                        duas_sequencias += 1

                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO

                    if duas_sequencias >= 2:
                        return (l, c)
                    
        
        # REGRA 3:
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)
        
       # REGRA 4:
        cantos = [(0, 0), (2, 2), (0, 2), (2, 0)]
        opostos = [(2, 2), (0, 0), (2, 0), (0, 2)]
        for i in range(len(cantos)):
            l, c = cantos[i]
            if self.matriz[l][c] == 4:
                l_oposto, c_oposto = opostos[i]
                if self.matriz[l_oposto][c_oposto] == Tabuleiro.DESCONHECIDO:
                    return (l_oposto, c_oposto)
                
      # REGRA 5:
        for i in range(len(cantos)):
            l, c = cantos[i]
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)

      # REGRA 6:
        lista = [
            (l, c) for l in range(3) for c in range(3)
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO
        ]

        if lista:
            p = randint(0, len(lista) - 1)
            jogada = lista[p]
            return jogada

        return None
