# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


def twosum(nums,target):

    dic = {}
    result = []
    for index, num in enumerate(nums):
        a = target - num
        if a not in dic:
            dic[num] = index
        else:
            result.append([dic[a], index])
    return result


if __name__ == '__main__':
    nums = [2, 7, 3, 6, 11, 15]
    target = 9
    print(twosum(nums, target))