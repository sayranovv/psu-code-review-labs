# https://www.perplexity.ai

with open('FileName1', 'r', encoding='utf-8') as fin:
    n = int(fin.readline())
    m = [list(map(int, fin.readline().split())) for _ in range(n)]
    k1, k2 = map(int, fin.readline().split())

k1 -= 1
k2 -= 1

paths = []
used = [False] * n
path = []

def dfs(v):
    used[v] = True
    path.append(v + 1)

    if v == k2:
        paths.append(path.copy())
    else:
        for to in range(n):
            if m[v][to] == 1 and not used[to]:
                dfs(to)

    path.pop()
    used[v] = False

dfs(k1)

paths.sort(key=lambda p: (len(p), p))

with open('FileName2', 'w', encoding='utf-8') as fout:
    if not paths:
        fout.write('-1')
    else:
        fout.write(str(len(paths)) + '\n')
        for p in paths:
            fout.write(' '.join(map(str, p)) + '\n')