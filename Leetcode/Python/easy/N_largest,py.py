

def third_largest(array: list):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0

    for i in array:
        if i > num1:
            num4 = num3
            num3 = num2
            num2 = num1
            num1 = i
        elif i > num2:
            num4 = num3
            num3 = num2
            num2 = i
        elif i > num3:
            num4 = num3
            num3 = i
        elif i > num4:
            num4 = i
    return num2


if __name__ == '__main__':
    arr = [1, 2, 5, 3, 2]
    print(third_largest(arr))