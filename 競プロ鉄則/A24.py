'''
問題


URL 
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_x

入出力例
input: 
6
2 3 1 6 4 5

output:
4

'''
import bisect

def main():
    N = int(input())
    A = list(map(int, input().split()))

    LEN = 0
    L = []
    dp = [None] * N

    for i in range(N):
        pos = bisect.bisect_left(L,A[i])
        dp[i] = pos

        if dp[i] >= LEN:
            L.append(A[i])
            LEN += 1
        else:
            L[dp[i]] = A[i]
        
    
    
    print(LEN)

if __name__ == "__main__":
    main()