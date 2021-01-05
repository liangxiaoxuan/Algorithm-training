# Find all duplicate patient_ID and print their index in increasing order
# Indexing starts at 1
# If there are no duplicate records, print 0


def duplicate(patient_id):

    dictId = {}
    for i in patient_id:
        if i in dictId:
            dictId[i] += 1
        else:
            dictId[i] = 1

    duplicate_ID = list(k for k, v in dictId.items() if v > 1)
    if not duplicate_ID:
        return 0
    else:
        result = []
        for index, value in enumerate(patient_id):
            if value in duplicate_ID:
                if index == 0:
                    continue
                else:
                    result.append(index)
    return result


if __name__ == '__main__':
    record = [[8],[8,42,11,6569,4],[2,28,12,6841,1],[4,9,14.631,2],[7,81,12.3156,2],
              [2,74,11,2714,1],[8,97,4.23856,1],[1,2,9.4435,2],[3,97,13.6312,1]]
    n = 9
    patient_id = []
    for i in range(n):
        patient_id.append(record[i][0])
    # 1 2 5 6
    print(duplicate(patient_id))


