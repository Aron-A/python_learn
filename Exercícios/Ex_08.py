def fatorial(n):

    fat = 1

    while n != 1 and n > 0:
        
        
        fat = fat * n 
        n = n - 1

    
    print(fat)


x = int(input("Digite um número inteiro: "))

fatorial(x)
