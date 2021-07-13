import random
import time 

# Intro into the game 


print( "(   .  (   ((   (     (( (       .  (   (        ( (  (   ((     )       (   (  (   (( " )  
print( ")\   . )\  ))\  )\   (\())\       . )\  )\       )\)\ )\  ))\   ())      )\: )\ )\  ))\  ")
print( "((_)__ ((_)((_)))(_)__)(_)(_)       ((_)((_)     (_)(_)_()((_)))(()))    ((_)((_)_()((_)))")
print( "| |/ // _ \| \| | |/ / __| _ \     / _ \| _ \    | || |   \ \| |/ __|    |  \/  |   \ \| |")
print( "|   <| (_) | .  |   <| _||   /    | (_) |   /    | __ | - | .  | (_ |    | |\/| | - | .  |")
print( "|_|\_\\___/|_|\_|_|\_\___|_|_\      \___/|_|_\    |_||_|_|_|_|\_|\___|    |_|  |_|_|_|_|\_|")

name=input ("Enter your Name: ")
print("What's Good? " + name + "! Best of Luck! " )
time.sleep(3)
print("Let the Games Begin!\n")
time.sleep(3)

# creating the main functions 
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = [
        "ivy", "cycle", "quiz", "staff", "gossip", "unknown", "jackpot", "flyby", "joyful", "nine"
    ]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = ' _ ' * length
    already_guessed = []
    play_game = ""

# loop to play the game again 

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y" or "Y":
        main()
    elif play_game == "n" or "N":
        print("Sad to see you go! Catch ya next time!")
        exit()

# conditons of the game !

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("What is the Hangman Word:  " + display + "  Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()      

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

    if count == 1:
            time.sleep(1)
            print("      ______  \n"
                  "     |        \n"
                  "     |        \n"
                  "     |        \n"
                  "     |        \n"
                  "     |        \n"
                  "     |        \n"
                  " ____|____\n" )
            print("Wrong guess mate. " + str(limit - count) + " guesses remaining\n")
  

    elif count == 2:
            time.sleep(1)
            print("      ______  \n"
                  "     |      |  \n"
                  "     |      |  \n"
                  "     |        \n"
                  "     |        \n"
                  "     |        \n"
                  "     |        \n"
                  " ____|____\n" )
            print("Try Again. " + str(limit - count) + " guesses remaining\n")

    elif count == 3:
            time.sleep(1)
            print("      ______  \n"
                  "     |      |  \n"
                  "     |      |  \n"
                  "     |      |  \n"
                  "     |        \n"
                  "     |        \n"
                  "     |        \n"
                  " ____|____\n" )
            print("Not your best performace. " + str(limit - count) + " guesses remaining\n")

    elif count == 4:
            time.sleep(1)
            print("      ______  \n"
                  "     |      |  \n"
                  "     |      |  \n"
                  "     |      |  \n"
                  "     |      O  \n"
                  "     |        \n"
                  "     |        \n"
                  " ____|____\n" )
            print("Come on Mate! " + str(limit - count) + " last chance!!\n")
        
    elif count == 5:
            time.sleep(1)
            print("      ______  \n"
                  "     |      |  \n"
                  "     |      |  \n"
                  "     |      |  \n"
                  "     |      O  \n"
                  "     |     /|\  \n"
                  "     |     / \  \n"
                  " ____|____\n" )
            print("AHH Nope, Sorry. You are Hanged!!\n")
            print("The word was:", already_guessed, word)
            play_loop()

    if word == '_' * length:
        print("Well done! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()
            
        
main()
hangman()