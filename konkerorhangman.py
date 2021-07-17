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
# the time code waits before excuting
time.sleep(2)
print("game loading...!")
time.sleep(3)
print("Let the Games Begin!!")
time.sleep(3)


words = ' ivy console camera awesome mother coding python warzone basketball earth future computer artificial coffee speaker mirror abstract glass moonlight'.split() 
#Random function 
def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

#Displaying the hangman graphics
def display_board(missed_letters, correct_letters, mystery_word):
    print(HANGINGMAN_GRAPHIC[len(missed_letters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()


#placing correctly guessed words in the spaces 
    blanks = '_' * len(mystery_word)

    for i in range(len(mystery_word)):
         if mystery_word[i] in correct_letters:
             blanks = blanks[:i] + mystery_word[i] + blanks[i+1:]

#Displaying the hangman word with spaces in between the letters
    for letter in blanks: 
        print(letter, end=' ')
    print()

#Error checking, making sure players enter a single letter
def get_guess(already_guessed):
     while True:
         print('Guess a letter.')
         guess = input()
         guess = guess.lower()
         if len(guess) != 1:
             print('Please enter a single letter.')
         elif guess in already_guessed:
             print('You have already guessed that letter. Choose again.')
         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             print('Please enter a LETTER.')
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

def play_again():
     print('Do you want to have another go? (yes or no)')
     return input().lower().startswith('y')

print('K O N K E R  O R  H A N G M A N !')
missed_letters = ''
correct_letters = ''
mystery_word = get_random_word(words)
game_is_done = False

#Checks if users guess is in the secret word
while True:
     display_board(missed_letters, correct_letters, mystery_word)

     guess = get_guess(missed_letters + correct_letters)

     if guess in mystery_word:
         correct_letters = correct_letters + guess

         # Checks if theres a win.
         found_all_letters = True
         for i in range(len(mystery_word)):
             if mystery_word[i] not in correct_letters:
                 found_all_letters = False
                 break
         if found_all_letters:
             print('Congrats Mate! The word is "' + mystery_word +
               '"! Well done!')
             game_is_done = True
     else:
         missed_letters = missed_letters + guess
         # Tells the user the amount of missed guesses 
         if len(missed_letters) == len(HANGINGMAN_GRAPHIC) - 1:
             display_board(missed_letters, correct_letters, mystery_word)
             print('Ahh Sorry mate! you have run out of guesses!\nAfter ' +
               str(len(missed_letters)) + ' missed guesses and ' +
               str(len(correct_letters)) + ' correct guesses, the word was "' + mystery_word + '"')
             game_is_done = True

#ask player if they wanna restart the game  
     if game_is_done:
         if play_again():
             missed_letters = ''
             correct_letters = ''
             game_is_done = False
             mystery_word = get_random_word(words)
         else:
             break

