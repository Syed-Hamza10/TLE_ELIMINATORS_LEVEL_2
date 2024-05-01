# problem link = https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/X

# def max_path_sum(matrix, i=0, j=0, path_sum=0):
#     rows, cols = len(matrix), len(matrix[0])
    
#     # Base case: if reached bottom-right cell
#     if i == rows - 1 and j == cols - 1:
#         return path_sum + matrix[i][j]
    
#     down_sum = 0
#     if i < rows - 1:
#         down_sum = max_path_sum(matrix, i + 1, j, path_sum + matrix[i][j])
    
#     right_sum = 0
#     if j < cols - 1:
#         right_sum = max_path_sum(matrix, i, j + 1, path_sum + matrix[i][j])
    
#     return max(down_sum, right_sum)

# # Example usage:
# matrix = [
#     [5, 2, 4],
#     [1, 3, 5],
#     [9, 2, 7]
# ]
# print(max_path_sum(matrix))


def path_sum(rows, cols,i = 0, j = 0, sum = 0 ):
    #base case: if we're at the right bottom
    if i == rows - 1 and j == cols - 1:
        return sum + m1[i][j]
    
    down = 0
    if i < rows - 1:
        down =  path_sum(rows,cols,i + 1, j, sum + m1[i][j])
    right = 0
    if j < cols - 1:
        right =  path_sum(rows,cols, i , j + 1, sum + m1[i][j])

    return max(down, right)

rows, cols = map(int,input().split())
m1 = []
for i in range(rows):          # A for loop for row entries
    a =[]
    for j in range(cols):      # A for loop for column entries
         a.append(map(int,input().split()))
    m1.append(a)
print(path_sum(rows, cols, ))


