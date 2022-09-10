from urllib.request import urlopen
import random


alphabet = "abcdefghijklmnopqrstuvwxyz" # alphabet

url = "https://www.dictionary.com/browse/" # url to dictionary

print("Welcome to the word generator and checker!")
print("Please enter a number between 1 and 10 to choose the length of the word you want to generate.")
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
        exit()
    else:
        print("The word is found in the dictionary.")
        exit()

if input_number < 10 or input_number > 1:
    rand_word = random.choices(alphabet, k=input_number) # generate a random word
    rand_word = ''.join(rand_word) # convert the list to a string
    print("Your word is: " + rand_word)
    print("Checking the word...")
    url = url + rand_word # add the word to the url
    response = urlopen(url) # open the url
    html = response.read() # read the html
    html = html.decode("utf-8") # decode the html
    try:
        if "No results found for " in html:
            print("The word is not found in the dictionary.")
        else:
            print("The word is found in the dictionary.")
    except:
        print("The word is not found in the dictionary.")
   