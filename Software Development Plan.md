
# Software Development Plan 

## Purpose of the Application 

    The purpose of "Konker or Hangman" is stimulate your mind and improve your vocabulary in a fun way. 
    Also guess the word/phrase before your man gets hanged! 

### Game Instructions

        On the Screen there are a number of dashes, equivalent to the length of the secret word. The goal is to correctly
        guess the secret word. If a guessing player correctly guesses a letter than is in the secret word, the computer 
        will place that letter in the right place in one of the dashes. If the letter does not appear in the secret word,
        then the computer will draw one element of a Hangmans Gallows. As the game continues, a feature of the Gallow and a victim is added for every incorrect guess not in the secret word. The number of incorrect guesses before the game ends with the victim hanged is seven. 




## Functions 

### Get Random word - 
        I've used the get random function to take a random word from my list for players to guess. 

### Display the board ( guessed words, missed guessed, secret word) - 
        It displays the current board, such as words guessed by the player so far and the words guessed wrong. secretword has no return value, its the word the player is trying to guess. 

### Get guess (already guessed ) - 
        takes a string of the players guessed letters and keeps asking for a letter that hasn't already been guessed. Returns the value of a the valid letter the player has guessed. 

### Play again - 
        Ask players if they would like to have another go. It will return True if yes or False and exits if no. 
