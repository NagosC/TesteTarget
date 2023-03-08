palavra = str(input('Digite uma palavra para invertermos: '))

def inverte(texto):
    return texto[::-1]

print(f'sua palavra invertida fica {inverte(palavra)}')