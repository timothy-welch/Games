import enchant
import random
d = enchant.Dict("en_US")
d.check("Hello")

###---- FUNCTIONS ----###

def split(word): #splits a word into individual letters in a list
    lst = []
    for i in word:
        lst.append(i)
    return lst

def unique(lst): #ensures that a list is filled with unique values
    if len(set(lst)) == len(lst):
        return True
    else:
        return False

def alpha(lst): #ensures list is filled with letters
    for i in lst:
        letter = i
        if not letter.isalpha():
            return False
    return True

def correct_length(attempt): #ensures attempt is correct length
    if len(attempt) < 4:
        return False
    else:
        return True
def used_correct_letters(attempt, pool, core): #ensures attempt uses correct letters
    if core not in attempt:
        return False
    for i in attempt:
        if i not in pool:
            return False
    else:
        return True

def make_word(lst): #creates a word from a list
    word = ''
    for i in range(len(lst)):
        letter = lst[i]
        word = word + letter
    return word
        
###---- INPUTS ----###
while True:
    core = input('Input core letter for the game: ')
    if len(core) == 1 and core.isalpha():
        break
    print('Core letter must be an individual letter')

while True:
    letters = input('Input 6 unique letters for the game: ')
    lst = split(letters)
    if core not in lst and unique(lst) and alpha(lst) and len(lst) == 6:
        break
    elif core in lst:
        print('Input letters must be different than core letter')
    elif not unique(lst):
         print('Input letters must be unique')   
    elif len(letters) != 6:
        print('Input must be 6 letters')
    elif not alpha(lst):
        print('Inputs must be alphabetical')

print('The game has begun! Try to build as many words as possible with the letter pool.')
print('The word must be at least 4 letters long and include the core letter. Good luck!')

###---GAME---###

pool = letters + core
pool = split(pool)
letters = split(letters)
correct = []
points = 0

while True:
    print('     Total points:', points ,',  Correct words: ', correct)
    print('     Core letter: ', core  , ',    Letter pool', pool)
    word = input('  "Shuffle" = shuffle letter pool. "Stop" = end game. \n Attempt?:  ')
    if word == 'Stop':
        break
    elif word == 'Shuffle': 
        random.shuffle(letters)
    else: 
        attempt = split(word)
        if used_correct_letters(attempt, pool, core) and correct_length(attempt) and alpha(attempt):
            if attempt not in correct and d.check(word):
                correct.append(word)
                length = len(attempt)
                if length == 4:
                    points += 1
                    print ('Nice! +1 Point')
                    print ('Total Points: ' , points)
                elif length == 5:
                    points += 3
                    print('Great! +3 Points')
                    print ('Total Points: ', points)
                elif length == 6:
                    points += 5
                    print('Impressive! +5 Points')
                    print ('Total Points: ', points)
                elif length > 6:
                    points += 10
                    print('Wow, really good one! +10 Points')
                    print ('Total Points: ', points)
        elif word in correct:
            print('You already got that one!')
        elif not used_correct_letters(attempt, pool, core):
            print('You have to use core letter and only use letters from the pool')
        elif not correct_length(attempt):
            print('Attempt is too short! Must be at least 4 letters')
        elif not alpha(attempt):
            print('Umm... it has to be letters')


print('Good round! Total points: ', points)            


