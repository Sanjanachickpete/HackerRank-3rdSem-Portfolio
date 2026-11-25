def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]

    return abs(primary_sum - secondary_sum)

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(diagonalDifference(arr))
