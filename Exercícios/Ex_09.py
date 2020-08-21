def impares(n):
      
    while n > 0:
       
        if n % 2 != 0:
            print(n)
        
        n = n - 1


x = int(input("Digite um número inteiro positivo: "))
        
impares(x)

