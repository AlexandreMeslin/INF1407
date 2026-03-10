#!/usr/bin/env python3

from retangulo import Retangulo
from ponto import Ponto

class Quadrado(Retangulo):
    def __init__(self, ponto=Ponto(), lado=10):
        '''
        Construtor da classe Quadrado.
        Inicializa um quadrado no plano cartesiano.
        O quadrado é representado por um ponto (canto inferior esquerdo) e um lado.

        :param self: Referência ao objeto atual da classe Quadrado.
        :param ponto: Ponto representando o canto inferior esquerdo do quadrado.
        :param lado: Comprimento do lado do quadrado.
        :return: None
        '''
        super().__init__(ponto, Ponto(ponto.x + lado, ponto.y + lado))  # Chama o construtor da classe Retangulo para inicializar o quadrado como um retângulo, utilizando o ponto fornecido e calculando o canto superior direito com base no comprimento do lado.
        return
    
    def __str__(self):
        '''
        Retorna uma representação em string do quadrado, no formato [p1, p2, p3, p4], onde p1, p2, p3 e p4 são os pontos que definem o quadrado.
        IMPORTANTE!!! O método str não exibe!!!

        :param self: Referência ao objeto atual da classe Quadrado.
        :return: Uma string representando o quadrado.
        '''
        return super().__str__()  # Chama o método __str__ da classe Retangulo para obter a representação em string do quadrado, que é a mesma do retângulo.
    
def main():
    quadrado = Quadrado()  # Cria uma instância da classe Quadrado, representando um quadrado no plano cartesiano.
    print(f'Quadrado: {quadrado}')  # Imprime a representação em string do quadrado.
    quadrado.p1 = Ponto(2,3)
    print(f'Quadrado: {quadrado}')  # Imprime a representação em string do quadrado.

if __name__ == '__main__':
    main()  # Chama a função main para executar os testes da classe Quadrado.