#problem link : https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/N

# def mat_sum(a, b, arr, cnt = 0):
#     if len(arr) == len(a):
#         print(arr)
#         return
#     arr.append(a[cnt] + b[cnt])
#     mat_sum(a,b,arr,cnt+1)

# R, C = map(int,input().split())

# a = list(map(int,input().split()))
# b = list(map(int,input().split())) 

# mat_sum(a, b,[])

# def sum_mat(m1, m2):
#     res = []

#     for i in range(len(m1)):
#         row = []
#         for j in range(len(m1)):
#             row.append(m1[i][j] + m2[i][j])
#         res.append(row)
#     return res



# def sum_rec(m1 , m2, i = 0, j = 0, res = [], row = []):
#     if i >= len(m1):
#         print(res)
#         return
#     if j >= len(m1[0]):
#         return
#     row.append(m1[i][j] + m2[i][j])
#     res.append(row)
#     #sum_rec(m1, m2, i, j + 1)
#     sum_rec(m1,m2, i+ 1, j, res, row)

# matrix1 = [[2, 4, 6],
#            [8, 10, 12],
#            [15, 15, 15]]

# matrix2 = [[9, 8, 7],
#            [6, 5, 4],
#            [15, 15, 15]]

# result = sum_rec(matrix1, matrix2)
# print(result)

