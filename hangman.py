# Hangman Step - 5

import hang_pic as hp
import words as wd
 
print(hp.logo)

import random

rand_word=random.choice(wd.words)
rand_word=rand_word.lower()

dash_list=[]
dl_word = ""
for i in rand_word:
    dash_list += "_"
    dl_word+="_ "

print(f"{dl_word} \n")

condition=True
life = 6
j=0
hang_condition=False

while (condition and not(hang_condition)):    
    guess=input("Enter a guess letter : ").lower()
    
    dl_word=""
    if(guess in dash_list):
            print(f"You've already guessed {guess}")
    for i in range(len(rand_word)):
        letter_position=rand_word[i]
        if(letter_position == guess):
            dash_list[i] = guess
            
        dl_word += dash_list[i]
        dl_word += " "

    print(f"{dl_word} \n")
    
    
    if(not(guess in dash_list)):
        life-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(hp.hangman[j])
        j+=1

    if(j==7):
        hang_condition=True
        
    condition=('_' in dash_list)

if(hang_condition):
    print("Game over ! you killed him..... ")
else:
    print("Congrats ! You saved him ........")
    
