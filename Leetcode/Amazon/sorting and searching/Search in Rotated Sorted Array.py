# You are given an integer array nums sorted in ascending order, and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# If target is found in the array return its index, otherwise, return -1.

# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# binary search

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start, end = 0, len(nums)-1  # pointers
    while start <= end:
        mid = start + (end-start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[end] >= target > nums[mid]:
                start = mid + 1
            else:
                end = mid -1
    return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    print(search(nums, target))