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

words_to_guess = ' ivy console camera awesome mother coding python warzone basketball earth future computer artificial coffee speaker mirror abstract glass moonlight'.split() 
#Random function 
def getRandomWord(wordlist):
    wordIndex = random.randit (0, len(wordlist) - 1)
    return wordlist[wordIndex]

#Displaying the hangman graphics
def displayBoard(missedLetters, correctLetters, secretWord): 
    print(HANGINGMAN_GRAPHIC[len(missedLetters)])
    print()

    print ('Missed letters:', end =' ')
    for letter in missedLetters:
        print(letter, end=' ')
        print()

    blank = '_' * len(secretWord)

#placing correctly guessed words in the spaces 
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

#Displaying the hangman word with spaces in between the letters
    for letter in blanks: 
        print(letter, end=' ' )
        print()

#Error checking, making sure players enter a single letter
def getGuess (alreadyGuessed):
    while True: 
        print('Pick a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1: 
            print('Please try a single letter. ')
        elif guess in alreadyGuessed:
            print ('Nope! you have already guessed that mane. Try another letter')
        elif guess not in 'abcdefghijklmnoqrstuvwxyz':
            print('Please enter a LETTER')
        else: 
            return guess  



# Loops to restart the Game:

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Sad to see you go! Catch ya soon!")
        exit()

# setting up the conditions needed for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("What is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()       


main()

hangman()
