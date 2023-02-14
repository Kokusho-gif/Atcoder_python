# 問題
# 2 つの文字列 S,T が与えられます。

# S に以下の 3 種類の操作のいずれかを順次実施して T に変換します。 そのような一連の操作のうち、最小の操作回数を求めてください。

# 操作
# ＜変更＞ S の中から文字 S_i を 1 つ選んで、その文字を好きな文字に変更します
# ＜削除＞ S の中から文字 S_i を 1 つ選んで、その文字を削除します
# ＜挿入＞ S の好きな箇所に好きな文字を挿入します

# URL 
# https://algo-method.com/tasks/315

# 入出力例
# input: 
# abc
# addc

# output:
# 2

def main():
    S = input()
    T = input()
        
    
    dp = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]

    for i in range(len(S)):
        for j in range(len(T)):

            if(i==0):
                if(S[i]==T[j]):
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]+1
            elif(j==0):
                if(S[i]==T[j]):
                    dp[i+1][j+1] = dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]+1
            else:
                if(S[i]==T[j]):
                    dp[i+1][j+1] = min(min(dp[i][j], dp[i+1][j]+1), dp[i][j+1]+1)
                else:
                    dp[i+1][j+1] = min(min(dp[i][j]+1, dp[i+1][j]+1), dp[i][j+1]+1)
    

    print(dp[len(S)][len(T)])



if __name__ == "__main__":
    main()