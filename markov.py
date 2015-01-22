#!/usr/bin/env python

from sys import argv
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    working_file = open(corpus)
    list_words = working_file.read().split()
    bigram_dict = {}

    for num in range(len(list_words)-2):
        word = list_words[num] 
        next_word = list_words[num + 1] 
        value = list_words[num + 2] 
        key_pair = (word, next_word) 
        
        if key_pair in bigram_dict:
            bigram_dict[key_pair].append(value)
        else:
            bigram_dict[key_pair] = [value]

    # for key, value in bigram_dict.nums():
    #     print key, value

    working_file.close()

    return bigram_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #Generating a random key pair to begin with
    random_key = random.choice(chains.keys())
    random_value = random.choice(chains[random_key])
    first_word = random_key[0]
    second_word = random_key[1]
    #Initializing beginning of string
    final_string = "%s %s" % (first_word, second_word)

    #reassigning random key generators to iterate through dictionary to lengthen final string
    #will exit loop once last random key generated is not found in dictionary and if final string length is under 140
    while random_key in chains and len(final_string) < 115:
        random_value = random.choice(chains[random_key])
        final_string += " %s" % random_value
        random_key = (random_key[1], random_value)

    #formatting final string to our specifications
    final_string = final_string.lower().capitalize()
    final_string_list = list(final_string)

    for num in range(len(final_string_list) -1):
        ch = final_string_list[num]
        if ch in "?.!":
            nch_index = num + 2
            final_string_list[nch_index] = final_string_list[nch_index].upper()

    
    final_string = "".join(final_string_list) + ". Namaste! -Obama Lama"
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
