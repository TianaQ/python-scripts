"""
My son needed more practice with multiplication 
and I made this little console game for him.
Launch with 

python mult_practice.py

in your terminal/command line and let your kids play too!
"""

import sys
import random

# numbers from 0 to 12
NUMBERS = tuple(range(13))

# probabilities for each number, adjust to your needs
WEIGHTS = (0.01, 0.01, 0.01, 0.05, 0.05, 0.03, 0.11,
           0.11, 0.11, 0.11, 0.05, 0.17, 0.18)

# response options for right and wrong cases
RESPONSE_CORRECT = ("Correct!", "That's right!", "Perfect!",
					"Good job!", "You're a genius!", "Great!")
RESPONSE_WRONG = ("Try again!", "No, it isn't...",
                  "Give it another try!", "Think twice...")

# these are for the hints in the game
FACTORS = {4: (2, 2), 6: (2, 3), 8: (2, 4), 9: (3, 3)}
DISTRIBUTIONS = {11: (10, 1), 12: (10, 2)}


def get_help(n1, n2):
    """
    For suitable numbers creates a representation by either its factors 
    or a sum of two numbers and returns an equation string with them.
    """
    def get_factors(n):
        if n in FACTORS:
            return [str(i) for i in FACTORS[n]]
        else:
            return False

    def distibute(n):
        if n in DISTRIBUTIONS:
            return [str(i) for i in DISTRIBUTIONS[n]]
        else:
            return False
    lst = []
    for n in [n1, n2]:
        s = " x ".join(get_factors(n)) if get_factors(n) \
        else "(" + " + ".join(distibute(n)) + ")" if distibute(n) \
        else str(n)
        lst.append(s)

    return " x ".join(lst)


def round_setup(numbers, weights):
    """
    For each round of the game randomly selects 2 numbers from the list 
    from 0 to 12 and returns the product of these two numbers to check 
    the player's input, the multiplication equation string and the equation 
    string with additional hints based on distibutive and associative 
    properties /see get_help() function/.
    """
    
    n1 = random.choice(random.choices(numbers, weights))
    n2 = random.choice(random.choices(numbers, weights))
    equation = "{} x {} = ".format(n1, n2)
    equation_help = get_help(n1, n2)
    product = n1 * n2
    return product, equation, equation_help


def attempt_to_answer(product, equation, equation_help, attempts=0):
    """
    Checks if the player's answer is correct and returns the number of attempt
    the player used before asnwering correctly. After 2 incorrect attempts 
    it prints the equation with additional helpful hints.
    """

    try:
    	answer = int(input())
    except:
    	print("Enter a number")
    	answer = -1
    attempts += 1

    if answer == product:
        print(random.choice(RESPONSE_CORRECT))
        return attempts
    elif answer == -1:
    	attempts -= 1
    	return attempt_to_answer(product, equation, equation_help, attempts)
    else:
        print(random.choice(RESPONSE_WRONG))
        if attempts > 1:
            print(equation + equation_help)
        return attempt_to_answer(product, equation, equation_help, attempts)

def play_round():
    """
    Launches the setup of each round, prints the equation for the round
    and returns the numbers of attempts the player took to pass the round.
    """

    product, equation, equation_help = round_setup(NUMBERS, WEIGHTS)
    print(equation)

    return attempt_to_answer(product, equation, equation_help)


def play_game():
    """
    Launches the math practice game. 
    Prompts the player to continue or stop every 10 rounds 
    and keeps track of the progress.
    """

    rounds = []

    while True:
        rounds.append(play_round())
        if len(rounds) % 10 == 0:
            check = input("Do you want to continue? (y/n)")
            if check == 'n':
                break
    total = len(rounds)
    first = sum(1 for r in rounds if r == 1)
    print(
    	"You got {} out of {} correctly at the first attempt!\nThat is {}%!" \
    	.format(first, total, round(100*first/total)))


def main():
    """
    Here starts the game!
    """
    
    print("\nHi! Let's start the multiplication practice game!")
    print("-------------------------------------------------\n")

    try:
        play_game()
    except:
        print("Unexpected input... exiting!\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
