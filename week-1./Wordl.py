from wonderwords import *
from rich.console import Console
from rich.text import Text
import os
import time


r = RandomWord()

to_guess = r.word(word_min_length=5, word_max_length=5)


console = Console()

guess = ""

print(to_guess)

def letters_check(guessed, word):
    main_l = [0, 0, 0, 0, 0]
    discard_l = [0, 0, 0, 0, 0]
    guessed_l = list(guessed)
    word_l = list(word)

    for i in range(len(guessed_l)):
        if guessed_l[i] in word:
            try :
                if guessed_l[i] == word_l[i] :
                    main_l[i] = [guessed_l[i], i]
                    continue
            except :
                pass
            main_l[i] = guessed_l[i]
        else :
            discard_l[i] = guessed[i]
    return [main_l, discard_l]

def print_guess(main) :

    full = [0, 0, 0, 0, 0]
    index_green = []
    index_gray = []
    index_orange = []

    for i in range(len(main[0])) :
        if isinstance(main[0][i], list):
            full[i] = main[0][i][0]
            index_green.append(i)
        else :
            if main[0][i] != 0 :
                full[i] = main[0][i]
                index_orange.append(i)
    
    for i in range(len(main[1])):
        if main[1][i] != 0:
            full[i] = main[1][i]
            index_gray.append(i)
    
    text_full = Text(''.join(full))


    for i in index_green:
        text_full.stylize("bold white on green", i, i + 1)
    for i in index_orange:
        text_full.stylize("bold white on yellow", i, i + 1)
    for i in index_gray:
        text_full.stylize("gray", i, i + 1)


    return text_full


buffer = []
i = 0

def display_buffer(buf) :
    os.system("clear")
    for dis in buf :
        console.print(dis)


os.system("clear")
print("Try and guess the 5 letter word\n")
guess = input("")
j = 0
while j == 0:
    if len(guess) != 5 :
            continue
    else :
        buffer.append(print_guess(letters_check(guess, to_guess)))
        display_buffer(buffer)
        j = 1
     


while (guess != to_guess and i <= 3) :
    guess = input("")
    if len(guess) != 5 :
        os.system("clear")
        print("It needs to be 5 letters long.\n")
        time.sleep(2)
        display_buffer(bufferedr)
        continue
    buffer.append(print_guess(letters_check(guess, to_guess)))
    display_buffer(buffer)
    i = i + 1

if i == 4 :
    print("\nBummer the word was : ", to_guess)
    exit()


display_buffer(buffer)

print("\n\ncongratulations, you found the word!")
