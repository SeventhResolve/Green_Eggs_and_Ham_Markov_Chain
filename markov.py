from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    text_string = open(file_path).read()

    return text_string 


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    bigram_third_word = []


    word_in_text = input_text.split()

    for each_word in range(len(word_in_text) - 2):
        first_and_second_words = word_in_text[each_word], word_in_text[each_word + 1]
        if first_and_second_words == (word_in_text[0], word_in_text[1]):
            chains[first_and_second_words] = bigram_third_word.append(word_in_text[2])
        # chains[first_and_second_words] = bigram_third_word
    #     if chains.get(first_and_second_words) != None:
    #         for each_word in range(len(word_in_text) - 2):
    #             third_word = word_in_text[each_word + 2]
    #         bigram_third_word.append(third_word)
    
    
    

    print chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
