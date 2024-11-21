def censor(text):
    forbidden_words = ["Java", "C#", "Ruby", "PHP"]

    words_list = text.split()

    censored_words = ["****" if word in forbidden_words else word for word in words_list]

    censored_text = " ".join(censored_words)

    return censored_text


print (censor("Java is the best, but PHP is the bester!"))

