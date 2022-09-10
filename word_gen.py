from urllib.request import urlopen
import random
from time import sleep

alphabet = "abcdefghijklmnopqrstuvwxyz" # alphabet

url = "https://www.dictionary.com/browse/" # url to dictionary

print("Welcome to the word generator and checker!")
print("If you want to check a word, enter 11.")
print("If you want to quit, enter 0.") 

input_number = int(input("Please enter a number: "))


if input_number == 0:
    print("Goodbye!")
    exit() # exit the program
if input_number == 11:
    print("Please enter a word: ")
    word = input()
    url = url + word
    response = urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    if "No results found" in html:
        print("The word is not found in the dictionary.")
        sleep(10)
        exit()
    else:
        print("The word is found in the dictionary.")
        sleep(10)
        exit()

class gen_num:
    rand_word = random.choices(alphabet, k=input_number) # generate a random word
    rand_word = ''.join(rand_word) # convert the list to a string
    print("Your word is: " + rand_word)
    print("Checking the word...")
    url = url + rand_word # add the word to the url
    try:
        response = urlopen(url) # open the url
        html = response.read() # read the response
        html = html.decode("utf-8") # decode the response
        if "No results found" in html:
            print("The word is not found in the dictionary.")
            sleep(10)
            exit()
        else:   
            print("The word is found in the dictionary.")
            sleep(10)
            exit()
    except:
        print("The word is not found in the dictionary.")
        sleep(10)
        exit()
