
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def convert_to_decimal(str_num: str, depart_system: int) -> int:

    for char in str_num:
        if char not in NUMBERS[:depart_system]:
            print("The number does not belong to the system. Please try again")
            return None

    result_num = 0


    for i, char in enumerate(str_num[::-1]):
        result_num += int(NUMBERS.index(char)) * depart_system ** i

    return result_num

def convert_from_decimal(num: int, arrive_system) -> str:

    decimal_num = num
    result_num = ""

    while decimal_num > 0:
        remainder = decimal_num % arrive_system
        result_num = NUMBERS[remainder] + result_num
        decimal_num = decimal_num // arrive_system
    return result_num

def convert_number(number: str, depart_system: int, arrive_system: int) -> str:
    decimal_number = convert_to_decimal(number, depart_system)
    arrived_number = convert_from_decimal(decimal_number, arrive_system)
    return arrived_number

def run_converter():
    while True:
        number = input("Please enter a number: ")
        depart_system = int(input("Please enter number system of this number: "))
        arrive_system = int(input("Please enter system you want to convert to: "))
        if depart_system > 16 or arrive_system > 16:
            print('The systems must be in range of 16')
            continue
        result = convert_number(number, depart_system, arrive_system)
        print(result)

run_converter()