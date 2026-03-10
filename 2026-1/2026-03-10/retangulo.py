#!/usr/bin/env python3

import ponto
from ponto import Ponto

class Retangulo:
    '''
    A classe Retangulo representa um retângulo no plano cartesiano,
    definido por dois pontos: o canto inferior esquerdo e o canto superior direito.
    '''
    def __init__(self, a=ponto.Ponto(), b=Ponto(1,1)):
        '''
        Construtor da classe Retangulo.
        Inicializa um retângulo no plano cartesiano.
        O retângulo é representado por dois pontos: o canto inferior esquerdo e o canto superior direito.

        :param self: Referência ao objeto atual da classe Retangulo.
        :param a: Ponto representando o canto inferior esquerdo do retângulo.
        :param b: Ponto representando o canto superior direito do retângulo.
        :return: None
        '''
        self.p1 = a
        self.p3 = b
        self.p2 = Ponto(self.p3.x, self.p1.y)
        self.p4 = Ponto(self.p1.x, self.p3.y)
        return
    
    def __str__(self):
        '''
        Retorna uma representação em string do retângulo, no formato [p1, p2, p3, p4], onde p1, p2, p3 e p4 são os pontos que definem o retângulo.
        IMPORTANTE!!! O método str não exibe!!!

        :param self: Referência ao objeto atual da classe Retangulo.
        :return: Uma string representando o retângulo.
        '''
        return f'[{self.p1}, {self.p2}, {self.p3}, {self.p4}]'
    
def main():
    retangulo = Retangulo()  # Cria uma instância da classe Retangulo, representando um retângulo no plano cartesiano.
    print(f'Retângulo: {retangulo}')  # Imprime a representação em
    print(f'Dir de retângulo: {dir(retangulo)}')  # Imprime a lista de atributos e métodos disponíveis para o objeto retangulo.

if __name__ == '__main__':
    main()  # Chama a função main para executar os testes da classe Retangulo.
