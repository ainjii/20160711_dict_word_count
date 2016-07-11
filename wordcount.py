# put your code here.

# Read each line in from file.
# Split by space character.
# Returns list of words without spaces.
# Iterate through list.
# Check if word is already in word-count dictionary.
# Add to current count if word appears again.

import string
# from collections import Counter
from sys import argv

def count_words(filename):
    testfile = open(filename)

    word_dictionary = {}

    for line in testfile:
        line = line.rstrip()
        wordlist = line.split()
        for word in wordlist:
            for char in string.punctuation:
                word = word.replace(char, "")
            word = word.lower()
            current_count = word_dictionary.get(word, 0)
            word_dictionary[word] = current_count + 1

    for word, count in word_dictionary.iteritems():
        print word, count


filename = argv[1]
count_words(filename)