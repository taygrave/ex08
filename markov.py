#!/usr/bin/env python

from sys import argv

script, working_file = argv 

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

    
    
    for key, value in bigram_dict.items():
        print key, value





make_chains(working_file)

    # return {}


# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

# def main():
#     args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

# if __name__ == "__main__":
#     main()
