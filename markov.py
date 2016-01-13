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


    word_in_text = input_text.split()

    for each_word in range(len(word_in_text) - 2):
        first_and_second_words = (word_in_text[each_word], word_in_text[each_word + 1])
        third_word = word_in_text[each_word + 2]
        if first_and_second_words in chains:
            chains[first_and_second_words].append(third_word)
        else:
            chains[first_and_second_words] = [third_word]
    
    

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    dict_keys = chains.keys()
    random_starting_key = choice(dict_keys)

    print random_starting_key

    # your code goes here
    # randomly select a key
    # while loop: randomly select an item from the value associated with that key
    # search for selected item in first position of dictionary keys
    # loop back to line 56 and keep doing it 
        #until you find Sam, I tuple
        #and print am?
        #break the loop
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
