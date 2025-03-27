import random

secret_number = random.randint(1, 100) #random number between 1 and 10
guess = None #your guess starts as none
while guess != secret_number: #keeps looping until you guess the secret number
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    if guess > secret_number:
      print ("too high")
    elif guess < secret_number:
      print ("too low")
    else:
      print ("correct!")