def max(a, b):

    if a > b :
        
        return a
    
    elif b > a:
         
        return b
    
    else:
        print("a = b = ", a)

x = int(input("Digite um número inteiro: "))
y = int(input("Digite um número inteiro: "))

max(x, y)