def eprimo(k):
    
    if k <= 2:
        
        k == int(input("Valor de x"))
        
    n = 2 
    primo = True
 
    while (n < k):
        d = k % n

        if (d == 0):
            primo = False
        n = n + 1
       
    if primo:
        lista.append(k)
        
    return primo

        

def n_primos(f):
    h = 3
    b = eprimo(f)
    if b:
       return f
    else:
        while (h != f):
            eprimo(h)
            h = h + 1
            
    return len(lista)        
        
x = int(input("Digite um número inteiro "))

lista = []

a = n_primos(x)



