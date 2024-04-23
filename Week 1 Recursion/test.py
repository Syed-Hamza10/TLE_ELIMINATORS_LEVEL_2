import sys
sys.setrecursionlimit(int(1e5))

def main():
    r,c = map(int, input().strip().split())
    print(r)
    print(c)
    mat1 = []
    mat2 = []
    res = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(r):
        mat1.append(list(map(int, input().strip().split())))

    for i in range(r):
        mat2.append(list(map(int, input().strip().split())))

    # dfs(0, 0, mat1, mat2, res)
    for row in res:
        for e in row:
            print(e, end=" ")
        print()

main()