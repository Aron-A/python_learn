def soma_dig(n):

    soma = 1

    while n > 1 :

        aux = n / 10

        soma = soma + aux

        n = aux
    
    print(soma)

x = int(input("Digite um número inteiro: "))

soma_dig(x)
