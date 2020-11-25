# you are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]


def rotate(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        res1 = []
        res2 = []
        res3 = []
        if len(matrix) == 1:
            return matrix

        if len(matrix) == 2:
            for i in matrix:
                res1.insert(0, i[0])
                res2.insert(0, i[1])
            return [res1, res2]
        else:
            for i in matrix:
                res1.insert(0, i[0])
                res2.insert(0, i[1])
                res3.insert(0, i[2])
            return [res1,res2,res3]


# inplace
def rotate2(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(matrix[i][j])
        matrix[i] = matrix[i][::-1]
    return matrix


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6],[7,8,9]]
    print(rotate2(matrix))
