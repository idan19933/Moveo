



secret_num = 6
guess_count = 0
while True:
    guess = input("Guess a number between 1 to 9: ")
    if guess == 'exit':
        exit()
    if  int(guess) > secret_num:
        print("Too high")
    elif  int(guess) < secret_num:
        print("Too low")
    elif int(guess) == secret_num:
        print("You won!")
        print(f"Number of guesses:{guess_count+1}")
        exit()
    guess_count += 1







