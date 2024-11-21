from coderslab import words
import random

def random_word(word_list):
    return random.choice(word_list)

print(random_word(words))