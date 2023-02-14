import sys
from typing import List
# 問題
# N 個の整数 A_0, ~ , A_N-1
# ​が与えられます (負の値もありえます)。
# これらの整数の中から何個かの整数を選んだときの、総和の最大値を求めてください。
# 
# ただし、何も選ばない場合の総和は 0 であるものとします。

# URL https://algo-method.com/tasks/307

# 入出力例
# input: 
# 3
# 7 -6 9 
# output:
# 16

def main():
    N:int = int(input())
    A:list[int] = list(map(int, input().split()))

    dp:list[int] = [0]*(N+1)

    dp[0] = 0

    for i in range(1,N+1):
        dp[i] = max(dp[i-1], dp[i-1]+A[i-1])
    
    print(dp[N])

    





if __name__ == "__main__":
    main()