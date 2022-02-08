def common_letters(x,y):
    letters = [] 
    for i in x:
        if i in y:
            letters.extend(i)
    letters = ",".join(letters)
    print("Common letters:" + str(letters))


