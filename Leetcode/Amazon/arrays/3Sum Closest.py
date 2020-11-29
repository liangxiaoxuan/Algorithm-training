# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    diff = inf
    for i in range(len(nums)):
        t = target - nums[i]
        n = nums[:i] + nums[i + 1:]
        a, b = 0, len(n) - 1
        while a + 1 < b:
            if abs(n[a] + n[b] - t) < abs(diff):
                diff = n[a] + n[b] - t
            if n[a] + n[b] > t:
                b -= 1
            elif n[a] + n[b] < t:
                a += 1
            elif n[a] + n[b] == t:
                return target
        if abs(n[a] + n[b] - t) < abs(diff):
            diff = n[a] + n[b] - t
    return target + diff


if __name__ == '__main__':

    threeSumClosest(nums, target)