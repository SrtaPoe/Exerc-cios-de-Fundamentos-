a = input('Digite um número: ')
b = input('Digite um número: ')
c = input('Digite um número: ')
if (a < b) and (a < c):
        MENOR = a
if (b < c):
        INTER = b
        MAIOR = c
else:
        INTER = c
        MAIOR = b
if (b < a) and (b < c):
        MENOR = b
if (a < c):
        INTER = a
        MAIOR = c
else:
        INTER = c
        MAIOR = a
if (c < a) and (c < b):
        MENOR = c
if (a < b):
        INTER = a
        MAIOR = b
else:
        INTER = b
        MAIOR = a
print(MAIOR, INTER, MENOR)
