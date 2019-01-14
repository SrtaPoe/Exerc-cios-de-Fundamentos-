NORTE = 2
NORDESTE = 3
CENTRO-OESTE = 4
SUL = 5
SIM = 1
NÃO = 0
d = input('Digite uma região: ')
r = input('A Viagem inclui volta: ')
if d ==  2 and r == 0:
    print(' A passagem custará R$ 500,00')
if d == 2 and r == 1:
    print(' A passagem custará R$ 900,00')
if d ==  3 and r == 0:
    print('A passagem custará R$ 350,00')
if d == 3 and r == 1:
    print('A passagem custará R$ 650,00')
if d == 4 and r == 0:
    print('A passagem custará R$ 350,00')
if d == 4 and r == 1:
    print('A passagem custará R$ 600,00')
if d == 5 and r == 0:
    print('A passagem custará R$ 300,00')
if d == 5 and r == 1:
    print('A passagem custará R$ 550,00')
