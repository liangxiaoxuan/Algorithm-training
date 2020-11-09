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
  

# 2.Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
### Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

def remove_duplicate(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    print(len(result), result)
    return print(result)

### Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def remove_duplicate2(nums):
    n = 0
    #while(n < len(nums)):
    for i in range(len(nums)):
        if nums[n] in nums[:n]:
            del nums[n]
        else:
            n += 1
    return nums



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

def remove_element(nums,val):
    n = 0
    for i in nums:
        if i == val:
            del nums[n]
        n += 1
    print(len(nums))


# 4.Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def Search_Insert_Position(nums, val):

    if val > max(nums):
        return len(nums)

    else:
        for i, num in enumerate(nums):
            if num == val:
                return i
            elif num < val:
                pass
            elif num > val:
                return i
  
# exp:
#     比如[1,3,5,6] target=4， 循环到3的时候，pass；循环到5的时候，5>target，插入target到5的左边，数组变成[1,3,4,5,6]，return target的index， 还是2


#11.06
# 5.Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def Maximum_Subarray(nums): # Kadane's algorithm

    currSum = nums[0]
    maxSum = nums[0]
    for i in range(1, len(nums)):
        currSum = max(nums[i], currSum + nums[i]) # 将前一个数加起来，比较若加起来和比自身小选自身数
        maxSum = max(maxSum, currSum) # 比较哪个subarray比较大
    print(maxSum)
    return maxSum

 


# 6.Plus One
# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

def

 

