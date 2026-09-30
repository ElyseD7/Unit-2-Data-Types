import random
x = random.randint(1, 100)
print(x)

guess = int(input("Guess a random number froom one to one-hundred "))

while True:
    if x > guess:
        print("Too low")
        guess = int(input("Guess a random number froom one to one-hundred "))
    elif x < guess:
        print("Too high")
        guess = int(input("Guess a random number froom one to one-hundred "))
    else:
        break

print("YOU WON")