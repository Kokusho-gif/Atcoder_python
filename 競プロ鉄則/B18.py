'''
問題

URL 
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cq

入出力例
input: 
3 7
2 2 3

output:
3
1 2 3
'''


def main():
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))

    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]

    dp[0][0] = 1

    for i in range(1,N+1):
        for j in range(S+1):
            if dp[i-1][j] == 1:
                dp[i][j] = 1
                if j+A[i-1] <= S:
                    dp[i][j+A[i-1]] = 1
    
    ans = []
    if dp[N][S] == 1:
        cur = S
        for i in range(N, 0, -1):
            if dp[i-1][cur] == 0:
                ans.append(str(i))
                cur -= A[i-1]
        
        ans.reverse()
        print(len(ans))
        print(" ".join(ans))

            
    else:
        print('-1')
    

if __name__ == "__main__":
    main()