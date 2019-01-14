i = int(input('Digite sua idade: '))
if i < 16:
    print('Não habilitado para votar')
elif i < 18 or i >= 65:
    print('Eleitor facultativo')
else:
    print('Eleitor obrigatório')
