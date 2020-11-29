# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if nums == None or len(nums) < 3:
        return []

    res = []

    n = len(nums)
    nums.sort()

    for i in range(n - 2):

        if i > 0 and nums[i] == nums[i - 1]:  ## ？？
            continue

        left = i + 1
        right = n - 1

        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ == 0:
                res.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif sum_ < 0:
                left += 1
            else:
                right -= 1

    return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))