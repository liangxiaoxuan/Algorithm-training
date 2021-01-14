### Kadane's algorithm
* So we assume that the largest subarray is the first element, then we go through A[1:] elements (all elements except the first one).
Kadane算法的执行流程，从头到尾遍历目标数组，将数组分割为满足上述条件的子串，同时得到各子串的最大前缀和，然后比较各子串的最大前缀和，得到最终答案。我们以array={−2, 1, −3, 4, −1, 2, 1, −5, 4}为例，来简单说明一下算法步骤。通过遍历，可以将数组分割为如下3个子串（-2），（1，-3），（4，-1，2，1，-5，4），这里对于（-2）这样的情况，单独分为一组。各子串的最大前缀和为-2，1，6，所以目标串的最大子串和为6

### Stack —— Last in First out
```python
# coding=utf-8
list = []
for i in range(10):
    list.insert(0,i) # 从index=0 插入value, 每次i都会从index = 0 开始插入，从前的value会往后退
    list.pop(0)  # 从index=0开始pop off一个value

```

### Dynamitc program ：An optimization over plain recursion 
* 动态规划： 优化遍历的复杂度
* Wherever we see a recursive solution that has repeated calls for same inputs, 
  we can optimize it using Dynamic Programming
  
* Compare two common substring:
```python
# coding=utf-8
# 2 string , find the longest common substring
# Dynamic programming

string1 = "Helloa"
string2 = "abcHello"
len1 = len(string1)
len2 = len(string2)

def commonsubstring(s1, l1, s2, l2):

    # create a zero value matrix
    dp = [[0 for x in range(l2+1)] for i in range(l1+1)]
    print dp
    result = 0

    for i in range(l1+1):   # 从i每一个跟同一个j对比
        for j in range(l2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1   # 对角数+1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result

```

### Binary Tree traversal:(二叉树遍历)
* Process of visiting each node in the tree exactly once in some order and reading data in 
a node 
*. breath-first (BFS) : Level 
  - 
  
   
*. depth-first (DFS)
 
 



