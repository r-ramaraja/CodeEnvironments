# Python3 program to convert
# integer value to roman values
# and roman values to interers

from nbformat import convert


def convertIntegerToRoman(number):
    """Function to convert integer to Roman Numerals
    Author: Ramaraja Ramanujan
    IDE: VS Code
    """
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1


def convertRomanToInteger(s):
    """Function to convert Roman Numerals to Integer
    Author: Ashrith Reddy Thukkaraju
    IDE: VS Code
    """
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
             'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman:
            num += roman[s[i:i+2]]
            i += 2
        else:
            num += roman[s[i]]
            i += 1
    return num


if __name__ == "__main__":
    number = 3549
    print("Roman value is:", end="\n")
    convertIntegerToRoman(number)
    print()
    roman = "CDXLIII"
    print("Integer value is:" + str(convertRomanToInteger(roman)), end="\n")
