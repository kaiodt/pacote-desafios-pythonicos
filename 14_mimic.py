"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import string
import random
import sys
from collections import defaultdict


def get_word_list(filename):
    with open(filename, 'r') as f:
        word_list = []
        for line in f:
            word_list += [word.strip(string.punctuation).lower()
                          for word in line.split()]

    return word_list


def mimic_dict(filename):
    """Retorna o dicionario imitador mapeando cada palavra para a lista de
    palavras subsequentes."""

    word_list = get_word_list(filename)
    mimic_dict = defaultdict(set)

    for i in range(len(word_list) - 1):
        mimic_dict[word_list[i]].add(word_list[i + 1])

    mimic_dict[''] = {word_list[0], }
    mimic_dict[word_list[-1]] = {'', }

    return mimic_dict


def generate_mimic_text(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    num_words = 200
    mimic_text = word

    for _ in range(num_words - 1):
        next_word = random.choice(list(mimic_dict[word]))
        mimic_text = ' '.join([mimic_text, next_word])
        word = next_word

    return mimic_text


# Chama mimic_dict() e print_mimic()
def main():
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    mimic_text = generate_mimic_text(dict, '')
    print(mimic_text)


if __name__ == '__main__':
    main()
