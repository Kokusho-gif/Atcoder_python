# 問題


# URL 
# https://algo-method.com/tasks/316

# 入出力例
# input: 
# 2 3
# 1 2 3
# 4 3 2
# output:
# 5 

def main():
    N, M = list(map(int, input().split()))
    c = [[0 for i in range(M)] for j in range(N)]

    for i in range(N):
        c[i] = list(map(int, input().split()))
        
    
    dp = [[0 for i in range(M+1)] for j in range(N+1)]

    for i in range(N):
        for j in range(M):
            if(i==0):
                dp[i+1][j+1] = dp[i+1][j] + c[i][j]
            elif(j==0):
                dp[i+1][j+1] = dp[i][j+1] + c[i][j]
            else:
                dp[i+1][j+1] = min(min(dp[i][j]+c[i][j], dp[i+1][j]+c[i][j]), dp[i][j+1]+c[i][j])

    print(dp[N][M])

if __name__ == "__main__":
    main()