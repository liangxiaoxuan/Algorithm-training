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
  
  
  
# 2. Given a 32-bit signed integer, reverse digits of an integer.
# Example:
# Input: x = 123
# Output: 321


