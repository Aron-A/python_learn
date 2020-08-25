def desenha(largura, altura):

    while (largura > 0):

        n = altura
        while n > 0:
            print("#", end = "")
            n = n - 1
        print()
        largura = largura - 1
        n = altura


colunas = int(input("Digite a largura: "))
linhas = int(input("Digite a altura: "))

desenha(colunas, linhas)