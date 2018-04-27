#!/usr/bin/python

import argparse
from itertools import chain
import numpy


def main(num_words, only_lowercase, only_alpha, leet, word_list_filename):

    word_list = load_word_list(word_list_filename)

    words = []
    separators = []
    for i in range(num_words):
        words.append(generate_word(word_list, only_lowercase))
        separators.append(generate_separator())


    if only_alpha:
        phrase = ' '.join(words)
    else:
        phrase = ''.join(list(chain(*zip(words, separators)))[:-1])

    if leet:
        phrase = leetify(phrase)

    print(phrase)

    return


def load_word_list(filename):

    word_list = {}

    with open(filename, 'r') as handle:
        entries = handle.readlines()

    for entry in entries:
        index, word = entry.split()
        word_list[index] = word

    return word_list


def generate_word(word_list, lowercase):

    dice = numpy.random.randint(1, 7, 5)
    index = ''.join(map(str, dice))
    word = word_list[index]

    return word if (lowercase or (numpy.random.random() > 0.5)) else word.capitalize()


SYMBOLS = ' ! @ # $ % & * - + = | : . / ? '


def generate_separator():

    index = numpy.random.randint(0, len(SYMBOLS))
    separator = SYMBOLS[index]

    return separator


TABLE = ''.maketrans('abcdefghijklmnopqrstuvwxyz', '48cd3f9h1jklmn0pqr57uvw6y2')


def leetify(source):

    leet = source.translate(TABLE)

    return leet


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--num-words', default=5, type=int, help='Number of words to generate [5]')
    parser.add_argument('-l', '--lower', default=False, action='store_true', help='All lowercase (no capitalization) [false]')
    parser.add_argument('-a', '--alpha', default=False, action='store_true', help='Only alpha characters (no symbols or numbers) [false]')
    parser.add_argument('-e', '--leet', default=False, action='store_true', help='U53 1337 5p34k [false]')
    parser.add_argument('-w', '--word-list', default='wordlist.txt', help='Word list filename [wordlist.txt')
    args = parser.parse_args()

    main(args.num_words, args.lower, args.alpha, args.leet, args.word_list)
