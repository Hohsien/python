import random

number = random.randint(0,100)
guess = -1
print("Guess the number!(0~100)")
while guess != number:
    guess = int(input("Is it... "))
 
    if guess == number:
        print("Hooray! You guessed it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")
