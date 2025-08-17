def dfs(x, xs, odd):
    s = sum(xs)
    if x == 10 or s >= 16:
        if xs and s <= 16:
            # print(xs)
            vs = []
            odd = 0
            for a in xs:
                if a & 1:
                    odd = a
                vs += [a] * (a // 2)
            # print(vs, odd)
            pal(vs, odd, 0)
        return
    dfs(x + 1, xs, odd)
    if odd or (x & 1) == 0:
        xs.append(x)
        dfs(x + 1, xs, False if x & 1 else odd)
        xs.pop()

ps = SortedList()

def pal(vs, odd, idx):
    if idx == len(vs):
        ps.add(int(''.join(str(v) for v in vs + ([odd] if odd else []) + vs[::-1])))
        return
    vis = set()
    for i in range(idx, len(vs)):
        if vs[i] not in vis:
            vis.add(vs[i])
            vs[i], vs[idx] = vs[idx], vs[i]
            pal(vs, odd, idx + 1)
            vs[i], vs[idx] = vs[idx], vs[i]

dfs(1, [], True)
# print(ps)

class Solution:
    def specialPalindrome(self, n: int) -> int:
        return ps[ps.bisect_right(n)]
