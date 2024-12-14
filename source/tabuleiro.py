# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]
        ]

    def tem_campeao(self):
        # Venceu na linha:
        for l in range(3):
            if sum(self.matriz[l]) == 12:
                return Tabuleiro.JOGADOR_X
            elif sum(self.matriz[l]) == 3:
                return Tabuleiro.JOGADOR_0
        
        # venceu na coluna:
        for c in range(3):
            if sum(self.matriz[l][c] for l in range(3)) == 12:
                return Tabuleiro.JOGADOR_X
            elif sum(self.matriz[l][c] for l in range(3)) == 3:
                return Tabuleiro.JOGADOR_0
            
        # venceu na diagonal principal:
        if sum(self.matriz[l][l] for l in range(3)) == 12:
            return Tabuleiro.JOGADOR_X
        elif sum(self.matriz[l][l] for l in range(3)) == 3:
            return Tabuleiro.JOGADOR_0
        
        # venceu na diagonal secundária:
        if sum(self.matriz[l][2 - l] for l in range(3)) == 12:
            return Tabuleiro.JOGADOR_X
        elif sum(self.matriz[l][2 - l] for l in range(3)) == 3:
            return Tabuleiro.JOGADOR_0
        return Tabuleiro.DESCONHECIDO
