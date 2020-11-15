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
#     比如[1,3,5,6] target=4， 循环到3的时候，pass；循环到5的时候，5>target，
#     插入target到5的左边，数组变成[1,3,4,5,6]，return target的index， 还是2

if __name__ == '__main__':
    nums = [1,2,4,5,6]
    val =3
    Search_Insert_Position(nums, val)
