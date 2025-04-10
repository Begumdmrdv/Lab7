import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# Test
if __name__ == "__main__":
    test = "Hello, world!"
    print("Reverse the sentence:", reverse_string(test))
    print("Capitalize the sentence:", capitalize_words(test))
    print("No Punctuation:", remove_punctuation(test))
