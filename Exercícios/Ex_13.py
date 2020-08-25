def vogcons(n):

    strg = str(n)
    vogal = ["a" , "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    if n in vogal:
        print("Vogal")
    
    else:
        print("Consoante")


x = input("Digite uma letra: ")

vogcons(x)



    
    
    
