import random

def random_sum():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print(f"The sum of dice is {num1} + {num2} = {num1 + num2}")
    return num1 + num2

def main_program():
    sum = random_sum()

    if sum == 7 or sum == 11:
        print("You won")
        return

    elif sum == 2 or sum == 3 or sum == 12:
        print("Casino won(")
        return

    else:
        goal = sum
        print(f"Now your goal number is {goal}")

    while True:
        new_sum = random_sum()

        if new_sum == 4 or new_sum == 7:
            print("You lose")
            break

        if new_sum == goal:
            print("You won")
            break

main_program()

