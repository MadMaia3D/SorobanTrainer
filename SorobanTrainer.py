import os
import random


def GetClamped(value_to_clamp: int, min_value: int, max_value: int) -> int:
    return max(min_value, min(value_to_clamp, max_value))


def Random_N_Digits_int(min_digits: int, max_digits: int) -> int:
    minimum_number = int(10 ** min_digits / 10)
    maximum_number = 0

    for i in range(max_digits):
        maximum_number += 9 * 10 ** i

    return random.randint(minimum_number, maximum_number)


def AdditionTraining (min_digits: int, max_digits: int) -> None:
    random_number_1: int = Random_N_Digits_int(min_digits, max_digits)
    random_number_2: int = Random_N_Digits_int(min_digits, max_digits)
    result = random_number_1 + random_number_2

    number_1_display: str = f"{random_number_1:_}".replace("_", ".")
    number_2_display: str = f"{random_number_2:_}".replace("_", ".")    
    result_display = f"{result:_}".replace("_", ".")

    input(f"{number_1_display} + {number_2_display} = ")    
    print(result_display)
    
    print("Press Enter to Continue...", end="")
    input()


def SubtractionTraining (min_digits: int, max_digits: int) -> None:
    random_number_1: int = Random_N_Digits_int(min_digits, max_digits)
    random_number_2: int = Random_N_Digits_int(min_digits, max_digits)
    
    if random_number_2 > random_number_1:
        random_number_1, random_number_2 = random_number_2, random_number_1
    
    result = random_number_1 - random_number_2
    
    number_1_display: str = f"{random_number_1:_}".replace("_", ".")
    number_2_display: str = f"{random_number_2:_}".replace("_", ".")
    result_display = f"{result:_}".replace("_", ".")

    input(f"{number_1_display} - {number_2_display} = ")
    
    print(f"{result_display}")
    input("Press Enter to Continue...")

def MultiplicationTraining (min_digits: int, max_digits: int) -> None:
    random_number_1: int = Random_N_Digits_int(min_digits, min_digits)
    random_number_2: int = Random_N_Digits_int(min_digits, max_digits)
    
    if random_number_2 > random_number_1:
        random_number_1, random_number_2 = random_number_2, random_number_1
    
    result = random_number_1 * random_number_2
    
    number_1_display: str = f"{random_number_1:_}".replace("_", ".")
    number_2_display: str = f"{random_number_2:_}".replace("_", ".")
    result_display = f"{result:_}".replace("_", ".")

    input(f"{number_1_display} x {number_2_display} = ")
    
    print(f"{result_display}")
    input("Press Enter to Continue...")


def digits_setup () -> tuple[int, int]:
    user_input_min: int = int(input("Please, enter the minimum number of digits for the operands: "))
    user_input_max: int = int(input("Please, enter the maximum number of digits for the operands: "))

    user_input_min = GetClamped(user_input_min, 1, 17)
    user_input_max = GetClamped(user_input_max, 1, 17)

    if user_input_min > user_input_max:
        user_input_min, user_input_max = user_input_max, user_input_min
    print(f"The minimum and maximum number of digits were respectively set to {user_input_min} and {user_input_max}")
    _ = input("Press enter to continue...")
    return (user_input_min, user_input_max)


def main() -> None:
    min_operand_digits: int = 1
    max_operand_digits: int = 3

    while (True):
        user_input: str = input("(A)ddition (S)ubtraction (M)ultiplication Setu(P) (Q)uit: ")

        if (len(user_input) != 0):
            user_input = user_input[0]
        else:
            user_input = '_'    

        match user_input.upper():
            case 'A':
                AdditionTraining(min_operand_digits, max_operand_digits)
            case 'S':
                SubtractionTraining(min_operand_digits, max_operand_digits)
            case 'M':
                MultiplicationTraining(min_operand_digits, max_operand_digits)
            case 'P':
                try:
                    min_operand_digits, max_operand_digits = digits_setup()
                except:
                    print("Invalid input, canceling operation ")
                    input("Press Enter to Continue...")
            case 'Q':
                break
        os.system('cls')


if __name__ == "__main__":
    main()