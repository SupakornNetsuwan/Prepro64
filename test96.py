"""Func"""

def findfact(number):
    """Find fact"""
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return fact

def wordcheck(guess_alphab, guess_vowels, waystomach):
    """Word checker"""
    if guess_alphab == 0:
        guess_alphab = 1
    elif guess_vowels == 0:
        guess_vowels = 1
    # print(guess_alphab, guess_vowels, waystomach)
    return guess_alphab*guess_vowels*waystomach

def func():
    """Alphabet match"""
    alphab = int(input()) #8
    pick_alphab = int(input()) #3
    vowels = int(input()) #4
    pick_vowels = int(input()) #2
    if pick_alphab > alphab:
        pick_alphab = alphab
    if pick_vowels > vowels:
        pick_vowels = vowels

    if pick_alphab == 0:
        guess_alphab = 0
    else:
        guess_alphab = findfact(alphab)//(findfact(pick_alphab)*findfact(alphab-pick_alphab)) #56

    if pick_vowels == 0:
        guess_vowels = 0
    else:
        guess_vowels = findfact(vowels)//(findfact(pick_vowels)*findfact(vowels-pick_vowels)) #6

    waystomatch = findfact(pick_alphab + pick_vowels) #120
    wordchecker = wordcheck(guess_alphab, guess_vowels, waystomatch)

    print("%d Alphabet" %(pick_vowels + pick_alphab))
    print("%d Word" %(int(wordchecker)))
func()
