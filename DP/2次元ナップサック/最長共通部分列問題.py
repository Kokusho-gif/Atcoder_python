# 問題
# 2 つの文字列 S,T が与えられます。

# S と T の共通の部分文字列となる文字列の長さの最大値を求めてください。

# ただし、 部分文字列は「文字列から文字を幾つか抜き出して順に繋げてできる文字列」を指します。 (たとえば、a, ad, abe は abcde の部分文字列です。)

# URL 
# https://algo-method.com/tasks/314

# 入出力例
# input: 
# abcde
# acbef

# output:
# 3 
def main():
    S : str = input()
    T : str = input()
    dp = [[0 for i in range(len(S)+1)] for j in range(len(T)+1)]

    for i in range(len(S)):
        for j in range(len(T)):
            if(S[i]==T[j]):
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
        print(dp[i])

    print(dp[len(S)])







if __name__ == "__main__":
    main()