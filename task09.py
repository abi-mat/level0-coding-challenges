vowel = "aeiouAEIOU"

def print_vowels(string):
    vow = [] 
    for i in string:
        if i in vowel:
            vow.extend(i)
    vow = ",".join(vow) 
    print("Vowels:" + str(vow))

