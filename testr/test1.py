#from sys import stdin

# res = {}
# stdin = [-2, -5, 3, 3, 3, 4]
# for line in stdin:
#     n = int(line)
#     if n in res:
#         res[n] += 1
#     else:
#         res[n] = 1
#
#
# max_value = res[max(res, key=res.get)]  # res.get
# tie_list = []
# for i in res:
#     if res[i] == max_value:
#         tie_list.append(i)
#
# sort_tie_list = sorted(tie_list, reverse=False)
# print(sort_tie_list[0])

s = [(1,2),(3,4)]
a = lambda x, y: min(x,y)
for x,y in s:
    b = a(x,y)
    print b

