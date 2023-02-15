# 問題


# URL 
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m

# 入出力例
# input: 
# 7 10
# 11 12 16 22 27 28 31

# output:
# 11mk

def main():
# 入力（A は 0 番目から始まることに注意）
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 配列の準備（R は 0 番目から始まることに注意）
    R = [ None ] * N

    # しゃくとり法
    for i in range(0, N-1):
        # スタート地点を決める
        if i == 0:
            R[i] = 0
        else:
            R[i] = R[i - 1]

        # ギリギリまで増やしていく
        while R[i] < N-1 and A[R[i]+1]-A[i] <= K:
            R[i] += 1

    # 出力
    Answer = 0
    for i in range(0, N-1):
        Answer += (R[i] - i)
    print(Answer)

if __name__ == "__main__":
    main()