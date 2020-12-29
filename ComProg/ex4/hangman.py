import random
word_list = ['python', 'java', 'kotlin', 'javascript']
word_choosen = random.choice(word_list)
guessing = '-' * len(word_choosen)
guessed = set()
print("H A N G M A N")
lives = 8
while lives:
    print("\n" + guessing)
    player = input("Input a letter: > ")
    if player in guessed:
        print("No improvements")
        lives -= 1
        continue
    if player not in word_choosen:
        print("No such letter in the word")
        lives -= 1
        continue
    for i in range(len(word_choosen)):
        if word_choosen[i] == player:
            guessing = guessing[0:i] + player + guessing[i+1:]
    guessed.add(player)
    if "-" not in guessing:
        break
if lives:
    print(f"\n{guessing}\nYou guessed the word!\nYou survived!")
else:
    print("You are hanged!")
