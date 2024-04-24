import os
import random


def GetClamped(value_to_clamp: int, min_value: int, max_value: int) -> int:
    return max(min_value, min(value_to_clamp, max_value))


def AdditionTraining () -> None:
    random_number_1: float = random.randint(0,999)
    random_number_2: float = random.randint(0,999)
    print(f"{random_number_1} + {random_number_2} = ", end="")
    result = random_number_1 + random_number_2
    input()
    print(f"{result}")
    print("Press Enter to Continue...", end="")
    input()


def SubtractionTraining () -> None:
    random_number_1: float = random.randint(0,999)
    random_number_2: float = random.randint(0,999)
    if random_number_2 > random_number_1:
        random_number_1, random_number_2 = random_number_2, random_number_1
    print(f"{random_number_1} - {random_number_2} = ", end="")
    result = random_number_1 - random_number_2
    input()
    print(f"{result}")
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
        user_input: str = input("(A)ddition (S)ubtraction Setu(P) (Q)uit: ")

        if (len(user_input) != 0):
            user_input = user_input[0]
        else:
            user_input = '_'    

        match user_input.upper():
            case 'A':
                AdditionTraining()
            case 'S':
                SubtractionTraining()
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