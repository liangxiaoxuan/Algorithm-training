# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    countN = dict.fromkeys(nums, 0)

    for i in nums:
        countN[i] += 1   # 先累积变成字典看各自多少
    print(countN)
    record_result = []
    for V in countN:
        each_value = []
        each_value.append(V)
        each_value.append(countN[V])
        record_result.append(each_value)

    record_result.sort(key=lambda x: x[1], reverse=True)
    print(record_result)

    final_result = []
    for i in range(k):
        #print(record_result[i][0])
        final_result.append(record_result[i][0])
    return final_result


if __name__ == '__main__':
    nums= [1, 2, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))
