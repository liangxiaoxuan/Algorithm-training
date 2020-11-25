# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
#
# Input: nums = [3,0,1]
# Output: 2


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    for i in range(1, len(nums)):
        expected_num = nums[i - 1] + 1
        if nums[i] != expected_num:
            return expected_num


if __name__ == '__main__':
    nums = [1,4,5]
    # print(nums[-1])
    missingNumber(nums)