### Day 7 Project: Hangman Project

<br>

<div align = center>
  <img src = "P7.gif">
</div>

<br>

### 1. Set Up the Game
- Prepare a list of words that the game can randomly choose from.
- Define the number of lives the player will have at the start.
### 2. Generate a Random Word
- Randomly select a word from the list.
- Generate blanks (_) equal to the number of letters in the word.
### 3. Gameplay Loop
- Start a loop to keep the game running until:
- The player fills all the blanks (wins), or
- The player runs out of lives (loses).
### 4. Prompt the Player
- Ask the player to guess a letter.
### 5. Check the Guessed Letter
- If the guessed letter is in the word:
- Reveal the letter in the appropriate blank(s).
- If the guessed letter is not in the word:
- Deduct one life from the player.
- Notify the player of the wrong guess and remaining lives.
### 6. Update Game State
- If all blanks are filled, declare the player as the winner.
- If the player has no lives left, end the game and reveal the correct word.
### 7. Display Progress
- Continuously show the current progress of the word with the guessed letters filled in and the remaining blanks.
### 8. End the Game
- If the player wins, congratulate them.
- If the player loses, reveal the correct word and end the game.

<br>

