# Exercício 01 

Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:
perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez

# Exercício 02 

Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:
A média aritmética é 5.5

# Exercício 03  (Par ou Impar)

Receba um número inteiro na entrada e imprima

par

quando o número for par ou

ímpar

quando o número for ímpar.

# Exercício 04  (Fizz)

Receba um número inteiro na entrada e imprima

Fizz

se o número for divisível por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

# Exercício 05 (Buzz)

Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

# Exercício 06  (FizzBuzz)

Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

# Exercício 07 

Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente

# Exercício 08  (Fatorial)

Escreva um programa que receba um número natural nn na entrada e imprima n!n! (fatorial) na saída.

# Exercício 09 

Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

Exemplo:

Digite o valor de n: 5
1
3
5
7
9

# Exercício 10 

Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Digite um número inteiro: 123

6

# Exercício 11 (Máximos)

Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

# Exercício 12 (Maior Primo)

Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

# Exercício 13 ( Vogais vs Consoantes)

Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função


# Exercício 14 

Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

#Exercício 15

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

# Exercício 16 (Removendo Repetidos)

Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

# Exercício 17 (Soma da Lista)

Escreva a função soma_elementos que recebe como parâmetro uma lista com números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.





# Adicional 1 (FizzBuzz)

Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

# Adicional 2 

Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

# Adicional 3 (Todos Primos)

Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

# Adicional 4 (Soma Hipotenusa)

Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, nn é uma hipotenusa se existem números inteiros ii e jj tais que:

n^2 = i^2 + j^2n 
2
 =i 
2
 +j 
2
 

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo nn e devolva a soma de todos os inteiros entre 1 e nn que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até nn testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

# Adicional 5 (Maior Element Lista)

Escreva a função maior_elemento que recebe como parâmetro uma lista com números inteirose devolve um número inteiro correspondente ao maior valor presente na lista recebida.

# Adicional 6 (Invertendo Sequência)

Como pedido na primeira video-aula desta semana, escreva um programa que recebe uma sequência de números inteiros e imprima todos os valores em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.





