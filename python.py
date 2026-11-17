print("Think of a number between 1 and 100.")
print("I will try to guess your number!")

low = 1
high = 100

while low <= high:
    guess = (low + high) // 2

    print("Is your number:", guess, "?")
    response = input("Enter (H) for higher, (L) for lower, (C) for correct: ").lower()

    if response == 'h':
        low = guess + 1
    elif response == 'l':
        high = guess - 1
    elif response == 'c':
        print("Yay! I guessed your number!")
        break
    else:
        print("Invalid input!")

if low > high:
    print("Your answers were incorrect!")