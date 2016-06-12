# Given a list of words, write a program to find the longest word made of other words in the list.
# Gayle Laakmann McDowell - Cracking the Coding Interview, 6th Edition

import collections


def can_be_build(word, is_original, ordered_words):
    if word in ordered_words and not is_original:
        return ordered_words[word]
    for i in range(1, len(word)):
        left = word[0:i]
        right = word[i:]
        if left in ordered_words.keys() and ordered_words[left] and can_be_build(right, False, ordered_words):
            return True
    ordered_words[word] = False
    return False

if __name__ == '__main__':
    words = {}
    with open("words.txt", "r") as file:
        for line in file:
            words[line.strip()] = True

    ordered_words = collections.OrderedDict(sorted(words.items(), key=lambda x: len(x[0]), reverse=True))
    copy_of_ordered_words = ordered_words.copy()

    for word in ordered_words:
        if can_be_build(word, True, copy_of_ordered_words):
            print(word)
            break


