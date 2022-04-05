import random
print("Hello! Ready to play the Number Guessing Game? You may Begin!")
number = random.randint(1,10)
chances = 0
print("Guess a number between 1 and 10")
while chances < 5:
    guessedNumber =  int(input("Enter the number you guessed."))
    if guessedNumber == number:
        print("YOU WON! CONGRAGULATIONS!")
        break
    elif guessedNumber < number:
        print("The number was too low! Guess a higher number than", guessedNumber)
    else:
        print("The number was too high! Guess a lower number than", guessedNumber)
    chances +=1
if not chances < 5:
    print("Oh No... You lost. Try again! The number was", number)