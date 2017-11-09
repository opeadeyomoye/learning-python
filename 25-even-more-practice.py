# breathing space

"""This function will split strings into words. I hope."""
def split_into_words(stringy):
    return stringy.split(' ')

"""Sorts the words"""
def sort_words(words):
    return sorted(words)

"""Prints the first word after popping it off"""
def print_first_word(words):
    print words.pop(0)

def print_last_word(words):
    print words.pop(-1)

"""Takes in a full sentence and returns the sorted words"""
def sort_sentence(sentence):
    return sort_words(split_into_words(sentence))

"""Prints the first and last words of a sentence"""
def print_first_and_last(sentence):
    words = split_into_words(sentence)

    print_first_word(sentence)
    print_last_word(sentence)
    return

"""Sorts the words, then prints the first and last"""
def print_first_and_last_sorted(sentence):
    sorted_words = sort_sentence(sentence)

    print_first_word(sorted_words)
    print_last_word(sorted_words)




