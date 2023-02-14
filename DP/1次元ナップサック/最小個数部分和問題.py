# 問題
# N 個の正の整数 A_0,…,A_N-1 と正の整数 M が与えられます。

# 総和が M となるようにいくつかの整数を選ぶ方法を考えます。 選ぶ必要のある整数の個数の最小値を求めてください。

# ただし、総和を M にすることができない場合は -1 と出力してください。

# URL 
# https://algo-method.com/tasks/311

# 入出力例
# input: 
# 5 12
# 7 5 3 1 8
# output:
# 2

def main():
    N, M = list(map(int, input().split()))
    A : list[int] =  list(map(int, input().split()))

    MOD = 1000

    
    dp : list[int] = [[0 for i in range(M+1)] for j in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 1

    for i in range(1,N+1):
        for j in range(1,M+1):
            dp[i][j] = dp[i-1][j]
            if((j-A[i-1]>=0) & (dp[i-1][j-A[i-1]]!=0)):
                if(dp[i-1][j]!=0):
                    dp[i][j] = min(dp[i-1][j-A[i-1]]+1, dp[i][j])
                else:
                    dp[i][j] = dp[i-1][j-A[i-1]]+1
    
    print(dp[N][M]-1)



if __name__ == "__main__":
    main()