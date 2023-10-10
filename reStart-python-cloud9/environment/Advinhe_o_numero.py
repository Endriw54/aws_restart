import random
number = random.randint(1,10)

print("Bem-vindo ao Adivinhe o número!")
print("As regras são simples. Vou pensar em um número e você tentará adivinhar")
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        for x in range(0,11):
            print(x)