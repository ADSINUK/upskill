"""
Turn the string 'Hello, World!' into 'WORLD HELLO!' using basic string
operations—no hard-coding the answer.  Then count the vowels in
'abracadabra' and assert the count is 5.
"""

original_string = "Hello, World!"
exclamation = original_string[-1]
new_string = original_string[:-1]
word_list = new_string.split(", ")
word_list.reverse()
final_sentence = " ".join(word_list) + exclamation
out = final_sentence.upper()

vowels = ["a", "e", "i", "o", "u"]
magic = "abracadabra"
vowel_count = 0
for letter in magic:
    if letter in vowels:
        vowel_count += 1
    else:
        vowel_count += 0

assert out == "WORLD HELLO!"
assert vowel_count == 5
