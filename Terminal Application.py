import random
import time 

# Intro into the game 

print(" (     (  ) )   ( .          ) )                .     ")    
print(" )\    )\(\( (  (\  (  ( (  (\(            )\ )\  (    ")     
print("(_)  ((())(|)\ (\  )\ )\)\  )(|          ((_)(_) )\   ")  
print("\ \    / /()\| |( )((_)_((_) ()\          |_   _|((_)  ")   
print(" \ \/\/ // -_) | _| _ \ '  \/ -_)           | | / _ \  ")  
print("  \_/\_/ \___|_|__|___/_|_|_|___|           |_| \___/  ")   
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
time.sleep(5)

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
    word =  random.choice(words_to_guess)
    length= len(word)
    count= 0
    display= '_' * length
    already_guessed = []
    play_game= ""

# loop to play the game again 

def play_loop():
    global play_game
    play_game = input( "Play Again?  y= yes, n= no \n")
    while play_game not in ("Y", "N", "y", "n"):
        play_game = input( "Play Again?  y= yes, n= no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Sad to see you go... Catch ya next time!!")
        exit()







