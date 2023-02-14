# 問題
# 重み付き有向グラフ G(V,E) について、以下の条件を満たす最短経路の距離を求めて下さい：

# ・ある頂点から出発し、出発点へ戻る閉路である。
# ・各頂点をちょうど１度通る。

# |V|, |E| はそれぞれグラフ G の頂点の数と辺の数を示す。グラフ G の頂点にはそれぞれ 0, 1, ..., |V|-1 の番号が付けられている。
# si, ti はグラフ G の i 番目の辺が結ぶ２つの頂点を表す（有向）。di は si と ti の間の距離　（i 番目の辺の重み）である。
# 最短経路の距離を1行に出力する。条件を満たす経路がない場合は -1 と出力する。

# URL 
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A&lang=ja


# 入出力例
# input: 
# 4 6
# 0 1 2
# 1 2 3
# 1 3 9
# 2 0 1
# 2 3 6
# 3 2 4

# output:
# 16

# 備考
# https://qiita.com/Ll_e_ki/items/fa475f5bb224ada9be97
import sys, math

def main():
    input = lambda: sys.stdin.readline()[:-1]
    def MI(): return map(int, input().split())
    inf = 10**18
    
    n,m = MI()
    cost = [[inf]*n for _ in range(n)]
    time = [[inf]*n for _ in range(n)]
    for i in range(m):
        s,t,d,ti = MI()
        s-=1; t-=1
        cost[s][t] = cost[t][s] = d
        time[s][t] = time[t][s] = ti
    
    dp = [[[inf, 0] for i in range(n)] for j in range(1<<n)]
    dp[0][0] = [0, 1]
    
    for bit in range(1<<n):
        for start in range(n):
            # if bit >> start & 0: continue
            for end in range(n):
                if bit >> end & 1: continue
                new = bit + (1<<end)
                
                if time[start][end] < dp[bit][start][0] + cost[start][end]: continue
                if dp[new][end][0] > dp[bit][start][0] + cost[start][end]:
                    dp[new][end][0] = dp[bit][start][0] + cost[start][end]
                    dp[new][end][1] = dp[bit][start][1]
                elif dp[new][end][0] == dp[bit][start][0] + cost[start][end]:
                    dp[new][end][1] += dp[bit][start][1]
    
    ans = dp[-1][0]
    if ans[0]==inf: print("IMPOSSIBLE")
    else: print(*ans)






if __name__ == "__main__":
    main()