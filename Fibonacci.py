num = int(input('Digite o valor a ser encontrado: '))
fibo = [0,1]
controler = True
cont = 0
acumulador = 0

while(controler):

    acumulador = fibo[cont] + fibo[cont + 1]

    fibo.append(acumulador)

    if(fibo[cont] == num):
        print(f'O número {num} pertence a sequencia de fibonacci')
        controler = False

    if(fibo[cont] > num):
      print(f'O número {num} não existe na sequencia de fibonacci')
      controler = False
    
    cont +=1