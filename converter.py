logo = """
░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""


# Basic colors
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"  
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

print(logo)
# Snippets
ask = green + '\n[' + white + '?' + green + '] '+ yellow
success = green + '\n[' + white + '√' + green + '] '
error = red + '\n[' + white + '!' + red + '] '
info= yellow + '\n[' + white + '+' + yellow + '] '+ cyan



def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    return decimal

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = decimal_to_octal(decimal)
    return octal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def decimal_to_octal(decimal):
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder + 55) + hexadecimal
        decimal //= 16
    return hexadecimal

def octal_to_decimal(octal):
    decimal = 0
    for digit in octal:
        decimal = decimal*8 + int(digit)
    return decimal

def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    binary = decimal_to_binary(decimal)
    return binary

def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    decimal = 0
    for digit in hexadecimal:
        if digit.isdigit():
            decimal = decimal*16 + int(digit)
        else:
            decimal = decimal*16 + ord(digit.upper()) - 55
    return decimal

def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = decimal_to_binary(decimal)
    return binary

def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    octal = decimal_to_octal(decimal)
    return octal

while True:
    print(f"{green}[1]{yellow} Binary to {red} Decimal")
    print(f"{green}[2]{yellow} Binary to {red} Octal")
    print(f"{green}[3]{yellow} Binary to {red} Hexadecimal")

    print(f"{green}[4]{yellow} Decimal to {red} Binary")
    print(f"{green}[5]{yellow} Decimal to {red} Octal")
    print(f"{green}[6]{yellow} Decimal to {red} Hexadecimal")

    print(f"{green}[7]{yellow} Octal to {red} Decimal")
    print(f"{green}[8]{yellow} Octal to {red} Binary")
    print(f"{green}[9]{yellow} Octal to {red} Hexadecimal")

    print(f"{green}[10]{yellow} Hexadecimal to {red} Binary")
    print(f"{green}[11]{yellow} Hexadecimal to {red} Octal")
    print(f"{green}[12]{yellow} Hexadecimal to {red} Decimal")
    print(f"{green}[13]{yellow} Exit")


    choice = input("Enter your choice (1-13): ")

    if choice == '1':
        binary = input(f"{green}Enter a binary number: " + green)
        decimal = binary_to_decimal(binary)
        print(f"The decimal equivalent of {red} {binary} is {decimal}")
    
    elif choice == '2':
        binary = input(f"{green}Enter a binary number: " + green )
        octal = binary_to_octal(binary)
        print(f"The octal equivalent of {red} {binary} is {octal}")
    
    elif choice == '3':
        binary = input(f"{green}Enter a binary number: " + green )
        hexadecimal = binary_to_hexadecimal(binary)
        print(f"The hexadecimal equivalent of {red} {binary} is {hexadecimal}")

    elif choice == '4':
        decimal = int(input(f"{green} Enter a decimal number: "))
        binary = decimal_to_binary(decimal)
        print(f"The binary equivalent of {red} {decimal} is {binary}")
    
    elif choice == '5':
        decimal = int(input(f"{green} Enter a decimal number: "))
        octal = decimal_to_octal(decimal)
        print(f"The octal equivalent of {red} {decimal} is {octal}")
    
    elif choice == '6':
        decimal = int(input(f"{green} Enter a decimal number: "))
        hexadecimal = decimal_to_hexadecimal(decimal)
        print(f"The hexadecimal equivalent of {red} {decimal} is {hexadecimal}")

    elif choice == '7':
        octal = input(f"{green} Enter an octal number: ")
        decimal = octal_to_decimal(octal)
        print(f"The decimal equivalent of {red} {octal} is {decimal}")
    
    elif choice == '8':
        octal = input(f"{green} Enter an octal number: ")
        binary = octal_to_binary(octal)
        print(f"The binary equivalent of {red} {octal} is {binary}")
    
    elif choice == '9':
        octal = input(f"{green} Enter an octal number: ")
        hexadecimal = octal_to_hexadecimal(octal)
        print(f"The hexadecimal equivalent of {red} {octal} is {hexadecimal}")
    
    elif choice == '10':
        hexadecimal = input(f"{green} Enter a hexadecimal number: ")
        binary = hexadecimal_to_binary(hexadecimal)
        print(f"The binary equivalent of {red} {hexadecimal} is {binary}")
    
    elif choice == '11':
        hexadecimal = input(f"{green} Enter a hexadecimal number: ")
        octal = hexadecimal_to_octal(hexadecimal)
        print(f"The octal equivalent of {red} {hexadecimal} is {octal}")
    
    elif choice == '12':
        hexadecimal = input(f"{green} Enter a hexadecimal number: ")
        decimal = hexadecimal_to_decimal(hexadecimal)
        print(f"The decimal equivalent of {red} {hexadecimal} is {decimal} ")

    elif choice == '13':
        print(f"{cyan} Exiting...")
        break

    else:
        print("Invalid choice. Please try again.\n")

