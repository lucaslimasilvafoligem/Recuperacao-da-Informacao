# -*- coding: utf-8 -*-
"""Cópia de Python - Revisão / Nivelamento.ipynb

Automatically generated by Colaboratory.
"""



"""# Python - Exercícios de Nivelamento

Se você quiser aprender um pouco de Python antes de fazer os exercícios, segue uma lista de tutoriais recomendados:

[Este notebook que vai desde o básico até o intermediário em python](https://github.com/arnaldog12/Jupyter-Tutoriais/blob/master/Python.ipynb).

[Tutorial Básico de Python](https://www.devmedia.com.br/python-tutorial/33274).

[Aprenda List Comprehension direto no navegador](https://www.programiz.com/python-programming/list-comprehension).

[Mais um tutorial de list comprehensions](https://pythonacademy.com.br/blog/list-comprehensions-no-python)

# List Comprehensions

Nos exercícios abaixo, use list comprehensions pra criar as listas de acordo com o que for pedido:

### Números pares até 30
"""

print([i for i in range(2, 32, 2)]);

"""<font color='red'>**Saída esperada:**</font>

```py
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
```

### Quadrado dos números ímpares até 10
"""

print([i*i for i in range(1, 10, 2)]);

"""<font color='red'>**Saída esperada:**</font>

```py
[1, 9, 25, 49, 81]
```

### Lucro obtido pela venda de um determinado produto por R$ 25.90, considerando diferentes valores de compra. Formatar saída com `'{:.2f}'.format(valor)`
"""

list_values = [13.80, 25.20, 17.70, 18.10]

list_profit = ['{:.2f}'.format(25.9 - valorCompra) for valorCompra in list_values];

list_profit

"""<font color='red'>**Saída esperada:**</font>

```py
['12.10', '0.70', '8.20', '7.80']
```

# Dictionary Comprehensions

Em Python, também é possível utilizar a mesma lógica das list comprehensions para criar dicionários. Portanto, crie os dicionários abaixo de acordo com o pedido no exercício.

### Chaves: números pares até 10; Valores: Cubo das chaves
"""

print({i: i**3 for i in range(2, 11, 2)});

"""<font color='red'>**Saída esperada:**</font>

```py
{2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}
```

### Chaves: elementos da lista; Valores: quantidade de vezes que o elemento apareceu na lista
"""

test_list = [3, 3, 2, 1, 1, 3, 2, 2, 1, 3, 0]

test_list.sort();

print({elemento: test_list.count(elemento) for elemento in test_list});

"""<font color='red'>**Saída esperada:**</font>

```py
{0: 1, 1: 3, 2: 3, 3: 4}
```

### Uma tupla ($x$, $y$), onde $x$ representa a i-ésima letra de uma string e $y$ = (i+1)-ésima letra
"""

string = 'python'

print([(string[i], string[i + 1]) for i in range(len(string) - 1)]);

"""<font color='red'>**Saída esperada:**</font>

```py
[('p', 'y'), ('y', 't'), ('t', 'h'), ('h', 'o'), ('o', 'n')]
```

# Funções

Crie uma função em python para cada instrução abaixo.

- **nome**: `by_six(x)`
- **entrada**: $x$ (número inteiro)
- **retorno**: booleano que indica se um número é divísivel por 6
"""

def by_six(x): return x % 6 == 0;

# não altere o código abaixo
test_list = list(range(15))
for x in test_list:
    print(x, by_six(x))

"""<font color='red'>**Saída esperada:**</font>

```py
0 True
1 False
2 False
3 False
4 False
5 False
6 True
7 False
8 False
9 False
10 False
11 False
12 True
13 False
14 False
```

- **nome**: `add_lists(list_1, list_2)`
- **entrada**: duas listas de números inteiros e de mesmo tamanho
- **retorno**: lista com a soma dos elementos na mesma posição
"""

#insira seu código aqui
def add_lists(list_1, list_2): return [list_1[i] + list_2[i] for i in range(len(list_1))];

# não altere o código abaixo
list_1 = [1, 2, 3, 4, 5]
list_2 = [7, 9, 6, 4, 0]

add_lists(list_1, list_2)

"""<font color='red'>**Saída esperada:**</font>

```py
[8, 11, 9, 8, 5]
```

- **nome**: `remove_character_from_word(word, char)`
- **entrada**: duas strings (`word` e `char`)
- **retorno**: string `word` sem os caracteres iguais a `char`
"""

def remove_character_from_word(word, char): return ''.join([i for i in word if i != char]);

# não altere o código abaixo
word = 'abracadabra'
remove_character_from_word(word, 'a')

"""<font color='red'>**Saída esperada:**</font>

```py
'brcdbr'
```

- **nome**: `simple_tokenization(sentence)`
- **entrada**: uma string representando uma frase
- **retorno**: conjunto de palavras da frase (sem repetição)

A **tokenização** é o processo de dividir uma sentença em uma lista de palavras. Nesse exercício, nós vamos implementar uma tokenização simples e alterá-la para que o resultado da nossa tokenização não tenha palavras repetidas.
"""

def simple_tokenization(sentence): return set(sentence.split());

# não altere o código abaixo
test_sentence = 'I love ice cream as much as I love myself'
simple_tokenization(test_sentence)

"""<font color='red'>**Saída esperada:**</font>

```py
{'I', 'as', 'cream', 'ice', 'love', 'much', 'myself'}
```
"""
