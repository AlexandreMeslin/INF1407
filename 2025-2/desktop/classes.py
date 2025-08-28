class Ponto:
    ''' classe Ponto:
    representa e manipula coordenadas x,y '''
    def __init__(self,x=0,y=0):
        ''' cria novo ponto (x,y) '''
        self.x = x
        self.y = y
        return

    def __str__(self):
        return f'({self.x},{self.y})'
        
p1 = Ponto()        # x = 0, y = 0
p2 = Ponto(3,4)     # x = 3, y = 4
p3 = Ponto(3)       # x = 3, y = 0
p4 = Ponto(y=4)     # x = 0, y = 4
p5 = Ponto(y=4, x=5)# x = 5, y = 4

print(f'Ponto 5 = {p5}')
