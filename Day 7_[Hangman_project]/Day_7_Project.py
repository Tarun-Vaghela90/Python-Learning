import random
# import Hangman_Words     #import all  
# import specific from source
from  Hangman_Words import logo, loose_logo , hanged_man , word_list, winner

#welcome Logo 
print(logo)

print("\n\n***************************************************************************************\n\n")

lives = 6
chosen_word = random.choice(word_list)

word_show = ''
word_length = len(chosen_word)
for position in range(word_length):
        word_show += "_"
game_over= False
correct_letter=[]
print("Guess The Word : "+word_show+"\n\n")
while not game_over:
    print(f'\n\n**************************  Lives Left { lives} / 6   ********************************************\n\n')
    guess = input("Guess A  Letter: ").lower()
    if guess in correct_letter:
        print(f"You Already Guessed {guess}")
        
    display =''
    for letter  in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives-=1
        print(f'You Guess {guess} that not in the word. You Loose  A  Life')
        if lives == 0:
            game_over=True
            print(f"************************************** IT WAS {chosen_word} *************************************************")
            print(loose_logo)
            print(hanged_man)
    if "_" not in display:
        game_over=True
        print(winner)
  

