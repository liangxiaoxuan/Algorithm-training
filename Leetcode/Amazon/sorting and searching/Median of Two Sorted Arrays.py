# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)

    result = sorted(nums1+nums2)  # 可用quicksort取代
    if (m+n) % 2 == 0:
        i = (m+n)//2      # 取整数部分 并作为索引
        median = (result[i-1] + result[i])/2
    else:
        i = (m+n+1)//2
        median = result[i-1]
    return median


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))
    print(12/10)
