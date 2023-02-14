from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        # parents[i] < 0　 == i is a root.

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

class Edge:
    def __init__(self, to, cap, rev):
        self.to = to
        self.cap = cap
        self.rev = rev

INF = 1 << 20

class FordFulkerson:
    def __init__(self, N):
        self.size = N
        self.g = [[] for _ in range(N)]

    def add_edge(self, a, b, c):
        g = self.g
        e = Edge(b, c, None)
        rev = Edge(a, 0, e)
        e.rev = rev
        g[a].append(e)
        g[b].append(rev)

    def dfs(self, i, goal, F):
        # ゴールに到着
        if i == goal:
            return F

        self.visited[i] = True

        for e in self.g[i]:
            # 容量 0 の辺は使えない
            if e.cap == 0:
                continue
            # 既に訪問した頂点に行かない
            if self.visited[e.to]:
                continue
            # 目的地までのパスを探す
            flow = self.dfs(e.to, goal, min(F, e.cap))
            # フローを流せる場合、残余グラフの容量を flow だけ増減させる
            if flow:
                e.cap -= flow
                e.rev.cap += flow
                return flow
        # すべての辺を探索しても見つからなかった
        return 0
    
    def show_capacity(self):
        for i, row in enumerate(self.g):
            print(f'vertex {i} : \n')
            for j in row:
                print(f'to : {j.to} cap: {j.cap}')

    def max_flow(self, s, t):
        ans = 0
        while True:
            self.visited = [False] * self.size
            F = self.dfs(s, t, INF)

            # フローを流せなくなったら操作終了
            if F == 0:
                break
            ans += F
        return ans
