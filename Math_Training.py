import os
import random


def AdditionTraining () -> None:
    random_number_1 = random.randint(0,999)
    random_number_2 = random.randint(0,999)
    print(f"{random_number_1} + {random_number_2} = ", end="")
    result = random_number_1 + random_number_2
    input()
    print(f"{result}")
    print("Press Enter to Continue...", end="")
    input()


def SubtractionTraining () -> None:
    random_number_1 = random.randint(0,999)
    random_number_2 = random.randint(0,999)
    if random_number_2 > random_number_1:
        random_number_1, random_number_2 = random_number_2, random_number_1
    print(f"{random_number_1} - {random_number_2} = ", end="")
    result = random_number_1 - random_number_2
    input()
    print(f"{result}")
    print("Press Enter to Continue...", end="")
    input()


while (True):
    user_input: str = input("(A)ddition (S)ubtraction (Q)uit: ")

    if (len(user_input) != 0):
        user_input = user_input[0]
    else:
        user_input = '_'    

    match user_input.upper():
        case 'A':
            AdditionTraining()
        case 'S':
            SubtractionTraining()
        case 'Q':
            break
    os.system('cls')