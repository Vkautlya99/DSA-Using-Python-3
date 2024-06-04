# Find the Vowels and Consonants in a String
sentence = "My name is Vikram"


def is_consonant(letter):
    vowel = "aeiouAEIOU"
    return letter.isalpha() and letter.lower() not in vowel


consonant = [i for i in sentence if is_consonant(i)]
print(consonant)
