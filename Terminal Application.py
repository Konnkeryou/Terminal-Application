import random
import time 

# Intro into the game 


print( "(   .  (   ((   (     (( (       .  (   (        ( (  (   ((     )       (   (  (   (( " )  
print( ")\   . )\  ))\  )\   (\())\       . )\  )\       )\)\ )\  ))\   ())      )\: )\ )\  ))\  ")
print( "((_)__ ((_)((_)))(_)__)(_)(_)       ((_)((_)     (_)(_)_()((_)))(()))    ((_)((_)_()((_)))")
print( "| |/ // _ \| \| | |/ / __| _ \     / _ \| _ \    | || |   \ \| |/ __|    |  \/  |   \ \| |")
print( "|   <| (_) | .  |   <| _||   /    | (_) |   /    | __ | - | .  | (_ |    | |\/| | - | .  |")
print( "|_|\_\\___/|_|\_|_|\_\___|_|_\      \___/|_|_\    |_||_|_|_|_|\_|\___|    |_|  |_|_|_|_|\_|")

name = input("Enter your name: ")
print("What's up " + name + "! Best of Luck!")
time.sleep(2)
print("game loading...!")
time.sleep(3)
print("Let the Games Begin!!")
time.sleep(3)


words = ' ivy console camera awesome mother coding python warzone basketball earth future computer artificial coffee speaker mirror abstract glass moonlight'.split() 
#Random function 
def get_random_word(word_list):
    word_index = random.randint (0, len(word_list) - 1)
    return word_list[word_index]

#Displaying the hangman graphics
def display_board(missed_letters, correct_letters, secret_word): 
    print(HANGINGMAN_GRAPHIC[len(missed_letters)])
    print()

    print ('Missed letters:', end =' ')
    for letter in missed_letters:
        print(letter, end=' ')
        print()

#placing correctly guessed words in the spaces 
    blanks = '_' * len(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

#Displaying the hangman word with spaces in between the letters
    for letter in blanks: 
        print(letter, end=' ' )
        print()

#Error checking, making sure players enter a single letter
def get_guess (already_guessed):
    while True: 
        print('Pick a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1: 
            print('Please try a single letter. ')
        elif guess in already_guessed:
            print ('Nope! you have already guessed that mane. Try another letter')
        elif guess not in 'abcdefghijklmnoqrstuvwxyz':
            print('Please enter a LETTER')
        else: 
            return guess  

# the hangman graphic
HANGINGMAN_GRAPHIC = [ '''
    +--------+
    | 
    |
    |
    |
    |
    |
 ___|____
|________| ''', '''
    +--------+
    |        +
    |        O
    |
    |
    |
    |
 ___|____
|________| ''', '''
    +--------+
    |        +
    |        O
    |        |
    |         
    |
    |
 ___|____
|________| ''', '''
    +--------+
    |        +
    |        O
    |      / |
    |         
    |
    |
 ___|____
|________| ''', '''
    +--------+
    |        +
    |        O
    |      / | \ 
    |         
    |
    |
 ___|____
|________| ''', '''
    +--------+
    |        +
    |        O
    |      / | \ 
    |       /   
    |
    |
 ___|____
|________| ''', '''
    +--------+
    |        +
    |        O
    |      / | \ 
    |       /  \  
    |
    |
 ___|____
|________| ''',]

# Loops to restart the Game:

def play_loop():
    print('Do you want to have another go? (yes or no)')
    return input().lower().startswith('y')

print('HANGMAN')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False 

while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess
#checks if the player has won
        found_all_letters = True
        for i in range(len(secret_word)): 
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Yeah boii!! The word is "' + secret_word + '"! You have Konkered!')
            game_is_done = True
    else:
        missed_letters = missed_letters + guess 

        if len(missed_letters) == len(HANGINGMAN_GRAPHIC) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('Ahh Sorry mate, You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(len(correct_letters)) + ' correct guesses, the word was " ' + secret_word + '"')
            game_is_done = True 
#ask player if they wanna restart the game 
    if game_is_done:
        if play_loop():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else: 
            break

