
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
    return result

# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.


def remove_duplicate2(nums):
    n = 0
    #while(n < len(nums)):
    for i in range(len(nums)):
        if nums[n] in nums[:n]:
            del nums[n]
        else:
            n += 1
    return nums


if __name__ == '__main__':
    nums = [1,2,3,4]
    remove_duplicate(nums)