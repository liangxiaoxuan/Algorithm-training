# Find all duplicate patient_ID and print their index in increasing order
# Indexing starts at 1
# If there are no duplicate records, print 0


def duplicate(patient_id):

    # dictId = {}
    # for i in patient_id:
    #     if i in dictId:
    #         dictId[i] += 1
    #     else:
    #         dictId[i] = 1
    #
    # duplicate_ID = list(k for k, v in dictId.items() if v > 1)
    # if not duplicate_ID:
    #     return 0
    # else:
    #     result = []
    #     for index, value in enumerate(patient_id):
    #         if value in duplicate_ID:
    #             if index == 0:
    #                 continue
    #             else:
    #                 result.append(index)
    # return result


# save index in dic and start from 1
    dictId = {}
    for i, v in enumerate(patient_id):
        if v in dictId:
            dictId[v].append(i+1)

        else:
            dictId[v] = [i+1]

    dup_list = []
    for i in dictId:
        if len(dictId[i]) > 1:
            dup_list = dup_list + dictId[i]

    final_list = list(sorted(dup_list))

    return final_list


if __name__ == '__main__':
    record = [[8,42,11,6569,4],[2,28,12,6841,1],[4,9,14.631,2],[7,81,12.3156,2],
              [2,74,11,2714,1],[8,97,4.23856,1],[1,2,9.4435,2],[3,97,13.6312,1]]
    patient_id = []
    for i in record:
        patient_id.append(i[0])
    # 1 2 5 6
    id_list = duplicate(patient_id)
    for i in id_list:
        print(i)


