def fizzbuzz(a):

    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    
    else:
        print(a)


x = int(input("Digite um número inteiro: "))

fizzbuzz(x)