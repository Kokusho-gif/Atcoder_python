# 問題
# n 個の行列の連鎖 M1,M2,M3,...,Mn が与えられたとき、スカラー乗算の回数が最小になるように積 M1M2M3...Mn の計算順序を決定する問題を連鎖行列積問題(Matrix-Chain Multiplication problem)と言います。
# n 個の行列について、行列 Mi の次元が与えられたとき、積 M1M2...Mn の計算に必要なスカラー乗算の最小の回数を求めるプログラムを作成してください。

# URL 
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B&lang=ja

# 入出力例
# input: 
# 6
# 30 35
# 35 15
# 15 5
# 5 10
# 10 20
# 20 25

# output:
# 15125

#備考
# https://atug.tokyo/?p=369


def main():
    n = int(input())
    size = [[0,0] for _ in range(n)]
    for i in range(n):
        size[i] = list(map(int, input().split()))
    
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 0
    

    # dp[i][j] = M_iからj個目のM_i+jまでの積の回数の最小値
    # jを一番外のループで行うのがポイント
    for j in range(1,n):
        for i in range(n-j):
            rc = size[i][0] * size[i+j][1]
            for k in range(1,j+1):
                tmp = dp[i][k-1] + dp[i+k][j-k]
                tmp += rc*size[i+k][0]
                if dp[i][j]>tmp:
                    dp[i][j] = tmp
    
    print(dp[0][n-1])


    


    





if __name__ == "__main__":
    main()