# 問題
# N 匹のうさぎがいます。 うさぎは 1 から N まで番号が振られています。
# これら N 匹のうさぎが徒競走をしました。 同着はいませんでした。 このとき、着順は N! 通り考えられます。
# 高橋君は M 人の観客から情報を集めました。 i 番目の観客によると、うさぎ x_i はうさぎ y_i よりも先にゴールしたそうです。
# すべての観客の情報に合致するような着順が何通り考えられるか求めてください。

# URL 
# https://atcoder.jp/contests/abc041/tasks/abc041_d

# 入出力例
# input: 
# 3 2
# 2 1
# 2 3

# output:
# 2

#備考
# トポロジカルソートの数え上げ
# N個の頂点集合の部分集合をN bitで表現する
# 101 => {1,3}, 11101 =>{1,3,4,5}
# dp[100] : 部分集合{1}のトポロジカルソートの通り数, dp[110] : 部分集合{1,2}のトポロジカルソートの通り数
# dp[S] = SUM(dp[S-{v_i}]) ; ただし,v_iはS-{v_i}からv_iへの有向辺がないようなv_i
# aからbへ有向辺がある == aはbより先にゴールした
 
def main():
    N,M = map(int, input().split())
    edge = [0 for i in range(N)]

    for i in range(M):
        x, y = map(int, input().split())
        edge[x-1] |= x,1<<(y-1)
    
    dp = [0 for i in range(1<<N)]
    dp[0] = 1

    for s in range(1, 1<<N):
        for i in range(N):
            if((s>>i)&1) and (not(edge[i]&s)): #二つ目の条件はedge[i]の条件を満たしているか
                dp[s]+=dp[s^(1<<i)]
    
    print(dp[-1])



if __name__ == "__main__":
    main()