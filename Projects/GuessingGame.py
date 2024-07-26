import random

secret_num = random.randrange(1, 10)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number: "))
    guess_count += 1
    
    if guess == secret_num:
        print(" ")
        print('You Win!')
        break
    else:
        print(" ")
        print("Try again")
        print(" ")
        
if secret_num != guess:
    print("You Lost!") 
    print(" ")
    print(f"The correct number was {secret_num}")