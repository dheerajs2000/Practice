#Finding the diagonal difference of a matrix
def diagonalDifference(arr):
    n=len(arr)
    sum1,sum2=0,0
    for i in range(n):
        sum1+=arr[i][i]
        sum2+=arr[i][n-1-i]
    return abs(sum1-sum2)
print(diagonalDifference([[11,2,3],[22,44,2],[33,6,1]]))
