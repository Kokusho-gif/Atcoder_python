# 問題
# N 個の正の整数 A_0,…,A_N-1 と正の整数 M が与えられます。

# いくつかの整数を選んで総和が M となるようにできますか。


# URL https://algo-method.com/tasks/309

# 入出力例
# input: 
# 3 10
# 7 5 3 

# output:
# Yes

def main():
    N, M = list(map(int, input().split()))
    A : list[int] =  list(map(int, input().split()))

    dp : list[int] = [[0 for i in range(M+1)] for j in range(N+1)]

    dp[0][0] = 1

    for i in range(1,N+1):
        for j in range(1,M+1):
            dp[i][j] = dp[i-1][j]
            if(j-A[i-1]>=0):
                dp[i][j] = max(dp[i-1][j-A[i-1]], dp[i][j])

    if(dp[N][M]): print('Yes')
    else: print('No')




if __name__ == "__main__":
    main()