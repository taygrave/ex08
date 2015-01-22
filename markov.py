#!/usr/bin/env python

from sys import argv
import random



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    working_file = open(corpus).read()
    list_words = working_file.split()
    bigram_dict = {}

    for item in range(len(list_words)-2):

        word = list_words[int(item)] 
        next_word = list_words[(int(item) + 1)] 
        value = list_words[(int(item) + 2)] 
        key_pair = (word, next_word) 
        
        if key_pair in bigram_dict:
            bigram_dict[key_pair].append(value)
        else:
            bigram_dict[key_pair] = [value]

    # corpus.close()
    # for key, value in bigram_dict.items():
    #     print key, value
    return bigram_dict


def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    random_key = random.choice(chains.keys())
    random_value = random.choice(chains[random_key])
    first_word = random_key[0]
    second_word = random_key[1]
    # print "%s %s %s" % (first_word, second_word, random_value)
    final_string = "%s %s %s" % (first_word, second_word, random_value)

    while random_key in chains:
        random_key = (random_key[1], random_value)
        if random_key in chains:
            random_value = random.choice(chains[random_key])
            final_string += " %s" % random_value
        else:
            break

    return final_string
 
def main():
    script, working_file = argv 
    # Change this to read input_text from a file
    input_text = working_file

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()

