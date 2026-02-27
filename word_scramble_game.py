

import random

words = ["apple", "python", "school", "computer", "student", 
         "science", "teacher", "rocket", "planet", "guitar"]
score = 0

print("Welcome to Word Scramble!")

while True:
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    
    print("\nScrambled word:", scrambled)
    attempts = 3
    
    while attempts > 0:
        guess = input(f"Guess the word ({attempts} tries left): ")
        
        if guess.lower() == word:
            print("Correct!")
            score += 1
            break
        else:
            attempts -= 1
            print("Wrong!")
            
    if attempts == 0:
        print("Out of tries! The word was:", word)
        
    print("Total Score:", score)

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break