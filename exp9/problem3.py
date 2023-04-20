import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "The quick brown fox jumps over the dog"
print(f"{string1} is pangram: {is_pangram(string1)}")
print(f"{string2} is pangram: {is_pangram(string2)}")
