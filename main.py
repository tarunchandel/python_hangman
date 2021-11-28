import random
import words
from ascii_arts import welcome_art, stages

print(welcome_art)
print("Get ready to play Hangman!")

level = int(input("Select 0 of easy and 1 for dificult: "))

if level == 0:
  word_list = words.words[0]
else:
    word_list = words.words[1]

word = random.choice(word_list)
blanks = len(word)
letters_of_word = []
vowels = ["a", "e", "i", "o", "u"]


for i in range(blanks):
  letters_of_word += "-"
 


wrong_guess_list = []
wrong_guess_count = 0
right_guess_list = []

def fill_vowels():
  for vowel in vowels:
    for i in range(blanks):
      letter = word[i]
      if letter == vowel:
        letters_of_word[i] = vowel

choice = input('Do you want fill in the vowels? Select "y" for yes.')
if choice == "y":
  fill_vowels()
else:
  vowels = []

while wrong_guess_count < 6 and ("-" in letters_of_word):
  print(' '.join(letters_of_word))
  letter_input = input("guess a letter\n").lower()
  
  #add a feature where user cannot repeat a letter
  if letter_input in wrong_guess_list or letter_input in right_guess_list or letter_input in vowels:
    print("Already used this letter")
  else:
    flag = False
    for i in range(blanks):
      letter = word[i]
      if letter == letter_input:
        #(print(letter))
        flag = True
        
        #remove it from word
        letters_of_word[i] = letter
        #add it to right_guess_list 
        #remove it from the list of available letters


    if not flag:
      wrong_guess_count += 1
      wrong_guess_list += letter_input
    else:
      right_guess_list += letter_input
    
    #print(f"wrong word count: {wrong_guess_count}\nWrong guesses: {' '.join(wrong_guess_list)}\nRight guesses: {' '.join(right_guess_list)}")
    print(stages[6-wrong_guess_count])


if wrong_guess_count < 6:
  print("Brilliant! You are the winner!")
else:
  print("Better luck next time.")
print(word)

