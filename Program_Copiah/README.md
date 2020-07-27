Prólogo

Neste último exercício da Parte 1, iremos praticar não só o que vimos até agora no curso mas também outra habilidade importante de um programador: utilizar e interagir com código escrito por terceiros. Aqui, você não irá implementar o seu programa do zero. Você irá partir de um programa já iniciado e irá completá-lo. Na verdade, esse é o caso mais comum na indústria de software, onde muitos desenvolvedores trabalham colaborativamente em um mesmo programa.
Introdução

Manuel Estandarte é monitor na disciplina Introdução à Produção Textual I na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH. Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.
Detecção de autoria

Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.
Traços linguísticos

Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

    Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
    Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    Complexidade de sentença: Média simples do número de frases por sentença.
    Tamanho médio de frase: Média simples do número de caracteres por frase.

Funcionamento do programa

A partir da assinatura conhecida de um portador de COH-PIAH, seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Os traços linguísticos que seu programa deve utilizar são calculados da seguinte forma:

    Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    
    Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 45=0.8
    Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 35=0.6
    Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
    Complexidade de sentença é o número total de frases divido pelo número de sentenças.
    Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).

Após calcular esses valores para cada texto, você deve compará-los com a assinatura fornecida para os infectados por COH-PIAH. O grau de similaridade entre dois textos, a a a e b b b, é dado pela fórmula:

Sab=∑i=16∣∣fi,a−fi,b∣∣6 S_{ab} = \frac{\sum_{i=1}^6 || f_{i,a} - f_{i,b} ||}{6} Sab​=6∑i=16​∣∣fi,a​−fi,b​∣∣​

Onde:

    Sab é o grau de similaridade entre os textos a e b;
    fi,a é o valor de cada traço linguístico i no texto a; e
    fi,b é o valor de cada traço linguístico i no texto b.

No nosso caso, o texto b b b não é conhecido, mas temos a assinatura correspondente: a assinatura de um aluno infectado com COH-PIAH. Ou seja, sabemos o valor de fi,b f_{i,b} fi,b​ que é dado como valor de entrada do programa.

Caso você não esteja acostumado com a notação matemática, podemos destrinchar essa fórmula da seguinte maneira:

Para cada traço linguístico i i i (tamanho médio da palavra, relação type-token etc.) se quer a diferença entre o valor obtido em cada texto dado (a a a) e o valor típico do texto de uma pessoa infectada (b b b): fi,a−fi,b f_{i, a} - f_{i, b} fi,a​−fi,b​

Dessa diferença se toma o módulo (∣∣…∣∣ || \ldots || ∣∣…∣∣), lembre-se da função abs do python.

Somamos os resultados dos 6 traços linguísticos (∑i=16\sum_{i=1}^6∑i=16​)

E por final dividimos por 6 ( x6 \frac{x}{6}6x​)

Perceba que quanto mais similares a a a e b b b forem, menor Sab S_{ab} Sab​ será. Para cada texto, você deve calcular o grau de similaridade com a assinatura do portador de COH-PIAH e, no final, exibir qual texto mais provavelmente foi escrito por algum aluno infectado (ou seja, o texto com assinatura mais similar à assinatura dada).

Exemplo:

Funções de suporte

Para facilitar seu trabalho, fornecemos para você um esqueleto do programa completo como base. Use-o! As funções definidas nele devem ser utilizadas no seu programa; algumas já estão implementadas, outras devem ser implementadas por você (conforme indicado pelo comentário "IMPLEMENTAR"). Sinta-se livre para criar funções adicionais, caso necessário.

Dica: não se preocupe com os detalhes de implementação das funções pré-prontas do esqueleto, como "separa_sentenca()", "separa_frase()" etc. nem com as definições exatas de frase e sentença. Essas funções já cuidam disso para você, e podem ser pensadas como "caixas pretas": você pode utilizá-las sabendo o que recebem e o que devolvem, mas não é necessário saber sobre os seus detalhes internos. Além de isso ser muito comum ao programar em equipe, usando essas funções você vai fazer o cálculo da maneira esperada pelo corretor automático.

Cuidado: A função le_textos() considera que um "texto" é uma linha de texto, ou seja, não é possível inserir parágrafos separados. Se você digitar algum "enter", a função vai entender que você está começando um novo texto. Preste especial atenção a isso se usar "copiar/colar" para inserir os textos! Note também que, no cálculo de similaridade, é preciso encontrar o valor absoluto de cada uma das diferenças.
Exemplo de Assinatura

Um passo importante para seu programa é calcular a assinatura dos textos corretamente. Para testar se sua função calcula_assinatura() está correta, deixamos aqui um exemplo de execução:

Concluindo

Basicamente, sua tarefa é implementar corretamente as seguintes funções:

    compara_assinatura(as_a, as_b)
    calcula_assinatura(texto)
    avalia_textos(textos, ass_cp)

Usando o esqueleto que oferecemos acima e implementando essas 3 funções, seu detector de plágio estará completo e você poderá submetê-lo ao corretor automático. Caso o corretor automático aponte erros, tente ler com bastante cuidado e atenção a mensagem fornecida por ele, pois ela normalmente ajuda a identificar o erro.

Boa sorte! Não desista!

Sabemos que é um desafio, mas você vai aprender muito com ele.

Pense no prazer que você vai sentir quando sua solução final for aceita!!! 
