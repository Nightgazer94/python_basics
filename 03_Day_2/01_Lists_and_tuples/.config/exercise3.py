names_list = ['itsy', 'bitsy', 'spider', 'climbed', 'up', 'the', 'waterspout']

def find_short_words(names):
    return [word for word in names if len(word) < 5]

print(find_short_words(names_list))


