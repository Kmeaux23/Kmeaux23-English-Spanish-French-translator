import csv

def intro():
  print('Welcome to my Spanish and French translator app.\nPlease type an Englsih word and press "Enter" for the translations.\nType "done" at any time to exit')

def exit():
  print(f'\nThank you for using my translator.\nI hope you learned some new words today!')

translations = {}

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish,french]

done = False

intro()

while not done:
  word = input("Type an English word you would like to translate: ")
  word = word.lower()
  
  if word == "done":
    done = True
    exit()

  

  elif word in translations:
    print(f'\nSPANISH: {translations[word][0]}')
    print(f'\nFRENCH: {translations[word][1]}')

  else:
    print("Try again...that word is not in our list.")