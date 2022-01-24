"""
Name(s): Sarah Silverman
Name of Project: The Great Encoder
"""
import os
# to clear: os.system("clear")
string_to_encode = 0
name = input("Greetings, what's your name? ")
print("Hello,", name+".")
mode = int(input("Type 1 to encode your own messages. Type 2 to play a game: "))
if mode == 1:
  type_of_cipher = str(input("Type the name of the cipher you would like to use. \nYour choices are:\nAtbash \nASCII \nCaesarean \nWhich one would you like to choose? "))
  if type_of_cipher.lower() == "atbash":
    def atbash():
      string_to_encode = str(input("Here you can encode your own message. What would you like to encode? Type it here: "))
      string_to_encode = string_to_encode.lower()
      list_to_encode = list(string_to_encode)
      i = ord('z') + ord('a')
      string_to_encode = ''
      string_to_encode = string_to_encode.join([chr(i - ord(x))for x in list_to_encode])
      os.system("clear")
      print("Your encoded message is", string_to_encode)
      return string_to_encode
    atbash()

  elif type_of_cipher.lower() == "ascii":
    def ascii1():
      string_to_encode = str(input("Here you can encode your own message. What would you like to encode? Type it here: "))
      string_to_encode = string_to_encode.lower()
      list_to_encode = list(string_to_encode)
      for index, item in enumerate(list_to_encode):
        list_to_encode[index] = str(ord(list_to_encode[index]))
      newstring = ''.join(list_to_encode)
      os.system("clear")
      print("Your encoded message is", newstring)
    ascii1()

  elif type_of_cipher.lower() == "caesarean":
    string_to_encode = input("Here you can encode your own message. What would you like to encode? Type it here: ")
    shift = int(input("This cipher works by shifting letters. By how much would you like to shift them? Enter it here: "))
    def caesar(string_to_encode, shift):
      newstring = ''
      for ch in string_to_encode:
        if ch.isalpha():
          moving = ord(ch) + shift
          if moving > ord('z'):
            moving -= 26
          finalletter = chr(moving)
        newstring += finalletter
      print("Your encoded message is", newstring)
      return newstring
    os.system("clear")
    caesar(string_to_encode, shift)
  
  elif type_of_cipher.lower() == "dog":
    os.system("clear")
    print("૮ ・ﻌ・ა")
    import sys
    sys.exit()


elif mode == 2:
  import random
  points = 0
  cipherorrandom = str(input("Welcome to the decoding game. If you would like to choose a specific cipher, type \"cipher\" here; otherwise type \"random\": "))
  list_of_words = ['dorsal', 'jargon', 'fencing', 'hangman','applesauce', 'meow', 'impostor', 'orangutan','random', 'words', 'randomness', 'letters', 'python', 'breakfast', 'java', 'computer', 'science', 'associating', 'freely', 'variable', 'string', 'list', 'numerous', 'linguine', 'halfwit', 'aragonite', 'calculus', 'derivative', 'integral', 'sine', 'cosine', 'tangent', 'algebra', 'beans', 'municipal', 'doodle', 'geometry', 'trigonometry', 'arithmetic', 'median', 'basketball', 'track']
  if cipherorrandom.lower() == "cipher":
    ciphertype = input("Choose a cipher: Atbash, ASCII, or Caesarean. \nType it here: ")
    if ciphertype.lower() == "atbash":
     os.system("clear")
     string_to_encode = random.choice(list_of_words)
     list_to_encode = list(string_to_encode)
     i = ord('z') + ord('a')
     string_to_encode = ''
     string_to_encode = string_to_encode.join([chr(i - ord(x))for x in list_to_encode])
     os.system("clear")
     print("Your encoded message is", string_to_encode,". Try to decode it.")
     word = str(input("Guess the word: "))
     while word.lower() != string_to_encode:
        print("Sorry, that is not correct.")
        word = str(input("Guess the word: "))
     if word.lower() == string_to_encode:
        print("Good job, you guessed correctly!")
    elif ciphertype.lower() == "ascii":
      os.system("clear")
      string_to_encode = random.choice(list_of_words)
      list_to_encode = list(string_to_encode)
      for index, item in enumerate(list_to_encode):
        list_to_encode[index] = str(ord(list_to_encode[index]))
      newstring = ''.join(list_to_encode)
      os.system("clear")
      print("Your encoded message is", newstring,". Try to decode it.")
      word = str(input("Guess the word: "))
      while word.lower() != string_to_encode:
        print("Sorry, that is not correct.")
        word = str(input("Guess the word: "))
      if word.lower() == string_to_encode:
        print("Good job, you guessed correctly!")
    elif ciphertype.lower() == "caesarean":
      os.system("clear")
      string_to_encode = random.choice(list_of_words)
      newstring = ''
      for ch in string_to_encode:
        if ch.isalpha():
          numbers = [1, 2, 3, 4, 5]
          shift = random.choice(numbers)
          moving = ord(ch) + shift
          if moving > ord('z'):
            moving -= 26
          finalletter = chr(moving)
        newstring += finalletter
      print("Your encoded message is", newstring,". Try to decode it.")
      word = str(input("Guess the word: "))
      while word.lower() != string_to_encode:
        print("Sorry, that is not correct.")
        word = str(input("Guess the word: "))
      if word.lower() == string_to_encode:
        print("Good job, you guessed correctly!")

  elif cipherorrandom.lower() == "random":
    list_of_ciphers = ['atbash', 'ascii', 'caesarean']
    cipher = random.choice(list_of_ciphers)
    if cipher == 'atbash':
     os.system("clear")
     string_to_encode = random.choice(list_of_words)
     list_to_encode = list(string_to_encode)
     i = ord('z') + ord('a')
     string_to_encode = ''
     string_to_encode = string_to_encode.join([chr(i - ord(x))for x in list_to_encode])
     os.system("clear")
     print("Your encoded message is", string_to_encode,". Try to decode it.")
     word = str(input("Guess the word: "))
     while word.lower() != string_to_encode:
        print("Sorry, that is not correct.")
        word = str(input("Guess the word: "))
     if word.lower() == string_to_encode:
        print("Good job, you guessed correctly!")
    elif cipher == 'ascii':
     os.system("clear")
     string_to_encode = random.choice(list_of_words)
     list_to_encode = list(string_to_encode)
     for index, item in enumerate(list_to_encode):
        list_to_encode[index] = str(ord(list_to_encode[index]))
        newstring = ''.join(list_to_encode)
        os.system("clear")
     print("Your encoded message is", newstring,". Try to decode it.")
     word = str(input("Guess the word: "))
     while word.lower() != string_to_encode:
        print("Sorry, that is not correct.")
        word = str(input("Guess the word: "))
     if word.lower() == string_to_encode:
        print("Good job, you guessed correctly!")

    elif cipher == 'caesarean':
      os.system("clear")
      string_to_encode = random.choice(list_of_words)
      numbers = [1, 2, 3, 4, 5]
      shift = random.choice(numbers)
      newstring = ''
      for ch in string_to_encode:
        if ch.isalpha():
          moving = ord(ch) + shift
          if moving > ord('z'):
            moving -= 26
          finalletter = chr(moving)
        newstring += finalletter
      os.system("clear")
      print("Your encoded message is", newstring,". Try to decode it.")
      word = str(input("Guess the word: "))
      while word.lower() != string_to_encode:
        print("Sorry, that is not correct.")
        word = str(input("Guess the word: "))
      if word.lower() == string_to_encode:
        print("Good job, you guessed correctly!")
  else:
    cipherorrandom = input("Sorry, that is not a valid option. Try again; type \"cipher\" or \"random\": ")

