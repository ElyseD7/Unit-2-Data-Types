import random
x = random.randint(1, 100)
print(x)

guess = int(input("Guess a random number froom one to one-hundred "))
guess_history = []

while True:
    if x > guess:
        print("Too low")
        guess = int(input("Guess a random number froom one to one-hundred "))
        guess_history.append(guess)
    elif x < guess:
        print("Too high")
        guess = int(input("Guess a random number froom one to one-hundred "))
        guess_history.append(guess)
    else:
        break

print("YOU WON")
print(guess_history)