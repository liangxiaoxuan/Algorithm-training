

def duplicatestring(string):

    res = []
    string = string.split(" ")
    for i in range(len(string)):
        if string[i] not in res:
            res.append(string[i])
        else:
            return string[i]


def countduplicate(string):
    res = {}
    stringg = string.split(" ")
    for i in stringg:
        if i not in res:
            res[i] = 1
        else:

            res[i] += 1


if __name__ == '__main__':
    string = "I am in the city which is in a"
    stringg = string.split(" ")

    #print(stringg)
    print(duplicatestring(string))
    #print(string[0])

