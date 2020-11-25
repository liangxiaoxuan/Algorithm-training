# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well
#
# Example
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    print(nums)
    return len(nums)

# Runtime: 80 ms, faster than 36.58%
# Memory Usage: 15.3 MB, less than 15.57%


if __name__ == '__main__':
    #nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    removeDuplicates(nums)
