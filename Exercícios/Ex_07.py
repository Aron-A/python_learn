def cresc(a, b, c):

    if a < b and b < c:
        print("crescente")
    
    else:
        print("não está em ordem crescente")


x = int(input("Digite um número inteiro: "))
y = int(input("Digite um número inteiro: "))
z = int(input("Digite um número inteiro: "))

cresc(x, y, z)