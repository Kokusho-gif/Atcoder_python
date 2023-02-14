# 問題
# N個の品物があります。i 番目の品物はそれぞれ重さと価値が w_i,v_iとなっています (0≤i≤N-1)。

# これらの品物から重さの総和が W を超えないように選んだときの、価値の総和の最大値を求めてください。

# URL 
# https://algo-method.com/tasks/308
# 入出力例
# input: 
# 6 9
# 2 3
# 1 2
# 3 6
# 2 1
# 1 3
# 5 85 

# output:
# 94 

def main():
    N, W = list(map(int, input().split()))
    w : list[int] = [0]*N
    v : list[int] = [0]*N
    for i in range(N):
        w[i], v[i] = list(map(int, input().split()))
    
    dp : list[list[int]] = [[0 for i in range(W+1)] for j in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,W+1):
            dp[i][j] = dp[i-1][j]
            if(j-w[i-1]>=0):
                dp[i][j] = max(dp[i-1][j-w[i-1]] + v[i-1], dp[i][j])

    print(dp[N][W])

            

            
    



    




if __name__ == "__main__":
    main()