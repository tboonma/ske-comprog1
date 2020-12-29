from mastermind import *

ball = Game()
round = 1
while True:
    guess = input("What is your guess?: ")
    if not guess.isnumeric():
        print("Please input as integer")
        continue
    print(f"Your guess is {guess}")
    print(ball.check(guess), "\n")
    if ball.check(guess) == '****':
        print(f"You solve it after {round} rounds")
        break
    round += 1
