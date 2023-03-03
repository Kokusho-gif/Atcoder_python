'''
問題


URL 
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_v

入出力例
input: 
7
2 4 4 7 6 7
3 5 6 7 7 7

output:
500

'''


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [-(10**9)]*(N+1)
    dp[1] = 0

    for i in range(1, N):
        dp[A[i-1]] = max(dp[A[i-1]], dp[i]+100)
        dp[B[i-1]] = max(dp[B[i-1]], dp[i]+150)
    
    print(dp[N])
            



if __name__ == "__main__":
    main()