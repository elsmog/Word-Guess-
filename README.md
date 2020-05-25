# Word Guess Game
### Final Project for Stanford's *Code in Place* Program
##### by Elyssa Kober

When the user plays WordGuess, the computer first selects a secret word at 
random from a list built into the program. The program then prints out a row 
of dashes— one for each letter in the secret word and asks the user to guess 
a letter. 

If the user guesses a letter that is in the word, the word is redisplayed 
with all instances of that letter shown in the correct positions, along with 
any letters correctly guessed on previous turns. 

If the letter does not appear in the word, the user is charged with an 
incorrect guess. The user keeps guessing letters until either (1) the user 
has correctly guessed all the letters in the word or (2) the user has made 
eight incorrect guesses.

The user’s guesses are acceptable in either lower or upper case, even though 
all letters in the secret words are written in upper case.

If the user guesses something that is more than a single character, or is a 
symbol or number, the program tells the user that the guess should only be 
a single, alphabetic character and asks for a new guess. It doesn't count the 
guess that was of an incorrect type as an incorrect guess. 

If the user guesses a correct letter more than once, the number of guesses 
left is not reduced. Guessing an incorrect letter a second time is counted as 
another wrong guess.  

The number of guesses the player initially starts with is determined by the 
constant INITIAL_GUESSES.

