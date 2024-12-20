
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def convert_to_decimal(str_num: str, depart_system: int) -> int:

    for char in str_num:
        if char.upper() not in NUMBERS[:depart_system]:
            print("The number does not belong to the system. Please try again")
            return None

    result_num = 0

    for i, char in enumerate(str_num[::-1]):
        char = char.upper()
        result_num += int(NUMBERS.index(char)) * depart_system ** i

    return result_num

def convert_from_decimal(num: int, arrive_system: int) -> str:

    decimal_num = num
    result_num = ""

    while decimal_num > 0:
        remainder = decimal_num % arrive_system
        result_num = NUMBERS[remainder] + result_num
        decimal_num = decimal_num // arrive_system
    return result_num

def convert_number(number: str, depart_system: int, arrive_system: int) -> str:
    decimal_number = convert_to_decimal(number, depart_system)
    if decimal_number is not None:
        arrived_number = convert_from_decimal(decimal_number, arrive_system)
        return arrived_number


def run_converter():
    while True:
        number = input("Please enter a number: ")
        arrive_system = input("Please enter system you want to convert to: ")

        params = number.split("x")
        if not len(params) == 2:
            print("Invalid number written. It must follow format 'NN...NNxS'")
            break

        number = params[0]
        depart_system = params[1]

        if depart_system.isdigit() and arrive_system.isdigit():
            depart_system = int(depart_system)
            arrive_system = int(arrive_system)
            if (depart_system > 16 or depart_system < 2) or (arrive_system > 16 or arrive_system < 2):
                print('The systems must be in range 2 to 16')
                continue
        else:
            print('The systems must be integers')
            continue

        result = convert_number(number, depart_system, arrive_system)
        print(result)

        command = input("Would you like to continue? (y/n): ")
        if command.upper() == 'N':
            break
        elif command.upper() == 'Y':
            pass
        else:
            print("Unrecognized command")

run_converter()