'''
問題


URL 
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u

入出力例
input: 
4
4 20
3 30
2 40
1 10

output:
60

'''


def main():
    N = int(input())
    A = [0]*(N+1)
    P = [0]*(N+1)

    for i in range(1,N+1):
        P[i], A[i] = list(map(int, input().split()))

    dp =[[None]*(N+1) for _ in range(N+1)]
    dp[1][N] = 0

    for LEN in reversed(range(0, N-1)):
        for l in range(1,N-LEN+1):
            r = l+LEN

            score1 = 0
            if l>=2 and l<=P[l-1]<=r:
                score1 = A[l-1]
            
            score2 = 0
            if r<=N-1 and l<=P[r+1]<=r:
                score2 = A[r+1]
            
            if l==1:
                dp[l][r] = dp[l][r+1] + score2
            elif r==N:
                dp[l][r] = dp[l-1][r] + score1
            else:
                dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1] + score2)
    
    Answer = 0
    for i in range(1, N+1):
        Answer = max(Answer, dp[i][i])
        print(dp[i][i])
    print(Answer)



if __name__ == "__main__":
    main()