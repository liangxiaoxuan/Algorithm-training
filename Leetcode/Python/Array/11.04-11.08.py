## 11.04

# 1.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

def twosum(nums, target):
    """
    :param nums:
    :param target:
    :return:
    """
    dic = {}
    result = []
    for index, num in enumerate(nums):
        a = target - num
        if a not in dic:  # append num into dic
            dic[num] = index  # if a !=  num
        else:
            result.append([dic[a], index])  # output is index

    print(result)


if __name__ == '__main__':
    nums = [1, 2, 7, 8, 9, 11]
    target = 9
    twosum(nums, target)
  

# 2.Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

def 



#11.05

# 3.Remove Element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.






# 4.Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

