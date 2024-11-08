NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E", "F"]

def convert_to_binary(str_num: str) -> int:
    if not str_num.isdigit():
        print("Unable to convert to decimal.")
        return None

    binary_num = int(str_num)
    result_num = ""

    while binary_num > 0:
        bin_remainder = binary_num % 2
        result_num = str(bin_remainder) + result_num
        binary_num = binary_num // 2
    return result_num

def convert_to_decimal(str_num: str) -> int:
    if not str_num.startswith("0b") and str_num[2:].isdigit():
        print("Unable to convert to binary. Please enter valid binary number.")
        return None


    decimal_num = str_num[2:][::-1]
    result_num = 0

    for i, char in enumerate(decimal_num):
        result_num += int(char) * pow(2, i)
    return result_num


def run_converter():
    while True:
        number = input("Please enter a number with a prefix: ")
        if number.startswith("0b"):
            result = convert_to_decimal(number)
            print("Your number in decimal form is: ", result)
        else:
            result = convert_to_binary(number)
            print("Your number in binary form is: ", result)

        command = input("Would you like to continue? (y/n)")
        if command == "n":
            break
        if command != "y":
            print("Unrecognized command. Please try again.")

run_converter()