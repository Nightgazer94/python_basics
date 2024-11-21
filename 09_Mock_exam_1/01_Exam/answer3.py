test_text = "racecar"

def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

a = palindrome(test_text)
print(a)