test_text = ["tomato", "tomatoes", "potato", "potatoes", "cars", "unicorns", "horse", "cow"]

def singulars_and_plurals(text):
    result = {
        "singulars": [],
        "plurals": []
    }
    for word in text:
        if word[-1] == "s":
            result["plurals"].append(word)
        else:
            result["singulars"].append(word)
    return result

a = singulars_and_plurals(test_text)
print(a)