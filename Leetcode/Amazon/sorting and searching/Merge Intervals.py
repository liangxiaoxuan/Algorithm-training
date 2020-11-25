# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    res = []
    i = 0
    while i < len(intervals):
        if i == len(intervals)-1:
            res.append(intervals[i])
            return res

        if intervals[i+1][0] < intervals[i][1]:
            res.append([intervals[i][0], intervals[i+1][1]])
            i += 1
        elif intervals[i][0] >= intervals[i+1][0]:
            res.append([intervals[i+1][0], intervals[i+1][1]])
            i += 1
        else:
            res.append(intervals[i])
        i += 1
    return res


if __name__ == '__main__':
    intervals = [[1,4],[0,4]]
    print(merge(intervals))
    #print(intervals[0][0])
