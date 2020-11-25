# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    num1 = 0
    num2 = 0

    for i in nums:
        if i > num1:
            num2 = num1
            num1 = i
        elif i > num2:
            num2 = i
    return num2


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))