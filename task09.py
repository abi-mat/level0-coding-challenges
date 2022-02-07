vowel = "aeiouAEIOU"

def print_vowels(string):
    for i in string:
        for j in vowel:
            if j == i:
                print("Vowel:" + i)

#Call function print_vowels and input string to output vowels

