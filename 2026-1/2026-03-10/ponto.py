#!/usr/bin/env python3
class Ponto:
    '''
    A classe Ponto representa um ponto no plano cartesiano, 
    definido por suas coordenadas x e y.
    '''
    def __init__(self, x=0, y=0):
        '''
        Construtor da classe Ponto.
        Inicializa um ponto no plano cartesiano.
        O ponto é representado por suas coordenadas x e y, 
        que são inicialmente definidas como 0.

        :param self: Referência ao objeto atual da classe Ponto.
        :return: None
        '''
        self.x = x  # Atributo de instância que representa a coordenada x do ponto, inicialmente definida como x.
        self.y = y  # Atributo de instância que representa a coordenada y do ponto, inicialmente definida como y.
        return

    def __str__(self):
        return f'[{self.x}, {self.y}]'  # Retorna uma representação em string do ponto, no formato (x, y).

    def __eq__(self, outro):
        '''
        Método de comparação de igualdade entre dois objetos da classe Ponto.
        Compara se as coordenadas x e y de dois pontos são iguais.

        :param self: Referência ao objeto atual da classe Ponto.
        :param outro: Outro objeto da classe Ponto a ser comparado.
        :return: True se as coordenadas x e y dos dois pontos forem iguais, False
        '''
        return self.x == outro.x and self.y == outro.y  # Compara se as coordenadas x e y do ponto atual são iguais às coordenadas x e y de outro ponto, retornando True se forem iguais e False caso contrário.

'''
Setor de testes da classe Ponto
'''
def main():
    '''
    Função que testa a classe Ponto.
    '''
    p1 = Ponto()  # Cria uma instância da classe Ponto, representando um ponto no plano cartesiano.
    p2 = Ponto(3,4)  # Cria outra instância da classe Ponto, representando outro ponto no plano cartesiano.
    p3 = Ponto(5)  # Cria mais uma instância da classe Ponto, representando mais um ponto no plano cartesiano.
    p4 = Ponto(y=6)  # Cria mais uma instância da classe Ponto, representando mais um ponto no plano cartesiano.
    p5 = Ponto(3,4)  # Cria mais uma instância da classe Ponto, representando mais um ponto no plano cartesiano, com as mesmas coordenadas de p2.

    print(f'Ponto 1: {p1}')  # Imprime as coordenadas do ponto p1.
    print(f'Ponto 2: {p2}')  # Imprime as coordenadas do ponto p2.
    print(f'Ponto 3: {p3}')  # Imprime as coordenadas do ponto p3.
    print(f'Ponto 4: {p4}')  # Imprime as coordenadas do ponto p4.
    print(f'Ponto 5: {p5}')  # Imprime as coordenadas do ponto p5.

    if p1 == p2:
        print('Ponto 1 é igual ao Ponto 2')  # Imprime uma mensagem indicando que o ponto p1 é igual ao ponto p2, caso as coordenadas x e y de ambos os pontos sejam iguais.
    else:
        print('Ponto 1 é diferente do Ponto 2')  # Imprime uma mensagem indicando que o ponto p1 é diferente do ponto p2, caso as coordenadas x e y de ambos os pontos sejam diferentes.
    if p2 == p5:
        print('Ponto 2 é igual ao Ponto 5')  # Imprime uma mensagem indicando que o ponto p2 é igual ao ponto p5, caso as coordenadas x e y de ambos os pontos sejam iguais.
    else:        
        print('Ponto 2 é diferente do Ponto 5')  # Imprime uma mensagem indicando que o ponto p2 é diferente do ponto p5, caso as coordenadas x e y de ambos os pontos sejam diferentes.   

if __name__ == "__main__":
    main()  # Chama a função main para executar o teste da classe Ponto.
