test_text = "Rage against the machine"

def shorter(text):
    return "".join((split_text[0] for split_text in text.split())).upper()

a = shorter(test_text)
print(a)