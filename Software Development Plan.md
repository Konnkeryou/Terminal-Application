
# Software Development Plan 

## Purpose of the Application 

The purpose of "Konker or Hangman" is stimulate your mind and improve your vocabulary in a fun way. 
The games objective is to guess the word/phrase before your man gets hanged!
The Target audience is anyone looking to kill time by playing a mind stimulating game.  

## System requirements
 
There are no system requirements for this game, it should just be able to run on any computer's terminal, although not tested in windows. 

## Running the game:
User should be able to run the game straight in the terminal by navigating to relative path and executing ( python3 konkerorhangman.py) 


### Game Instructions

On the Screen there are a number of dashes, equivalent to the length of the secret word. The goal is to correctly guess the secret word. If a guessing player correctly guesses a letter than is in the secret word, the computer will place that letter in the right place in one of the dashes. If the letter does not appear in the secret word, then the computer will draw one element of a Hangmans Gallows. As the game continues, a feature of the Gallow and a victim is added for every incorrect guess not in the secret word. The number of incorrect guesses before the game ends with the victim hanged is seven. 


## Functions 

### Get Random word - 
I've used the get random function to take a random word from my list for players to guess. 

### Display the board ( guessed words, missed guessed, secret word) - 
It displays the current board, such as words guessed by the player so far and the words guessed wrong. secretword has no return value, its the word the player is trying to guess. 

### Get guess (already guessed ) - 
takes a string of the players guessed letters and keeps asking for a letter that hasn't already been guessed. Returns the value of a the valid letter the player has guessed. 

### Play again - 
Ask players if they would like to have another go. It will return True if yes or False and exits if no. 


## User Interaction and Experience

The program starts with an introduction screen and then it asks the User to input there name. After, the game starts, the programs ask the user to guess a letter. 

***On the game screen***, it will display:

 "Guess a letter" (where it gives a chance for the user to input a guess.) 
 
 Ontop of this message is the "Missed letters" (which display the incorrect guessed letters the user has inputed.) 
 
 Then above that message is the HangMan Graphic ( which will evolve as the game progresses and if the user keeps inputing incorrect letters) 

 The game ends when either the user has correctly guessed the secret word or if he has run out of guesses and is hanged. At which point the program will ask if they would like to try again or exit the game. 

***Error Handling** 

If the user inputs a ***number*** the program prints "Please enter a LETTER". 

If the user inputs ***multiple letters*** the program prints "Please enter a single letter". 

If the user inputs an ***already guessed*** letter the program prints "You gave already guessed that letter. Choose again." 
