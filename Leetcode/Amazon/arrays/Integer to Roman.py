# Given a roman numeral, convert it to an integer

# Input: s = "IX"
# Output: 9

v = {"1": "I",
     "5": "V",
     "10": "X",
     "50": "L",
     "100": "C",
     "500": "D",
     "1000": "M",
     "4": "IV",
     "40": "XL",
     "400": "CD",
     "9": "IX",
     "90": "XC",
     "900": "CM"}


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanNum = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    string = ""
    for i in range(len(digits)):
        while num >= digits[i]:
            string += romanNum[i]
            num -= digits[i]
        if num <= 0:
            break
    return string


if __name__ == '__main__':
    num = 98
    print(intToRoman(num))
