vowels = "aeiouAEIOU"

def print_vowels(string):
    vowel = [] 
    for i in string:
        if i in vowels:
            vowel.extend(i)
    vowel = ",".join(vowel) 
    print("Vowels:" + str(vowel))

