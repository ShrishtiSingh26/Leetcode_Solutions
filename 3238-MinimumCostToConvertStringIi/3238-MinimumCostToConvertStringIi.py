# Last updated: 7/5/2026, 7:40:04 PM
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**18

        # Step 1: collect nodes
        nodes = set(original) | set(changed)
        idx = {s: i for i, s in enumerate(nodes)}
        n = len(nodes)

        # Step 2: Floyd–Warshall
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for o, c, w in zip(original, changed, cost):
            dist[idx[o]][idx[c]] = min(dist[idx[o]][idx[c]], w)

        for k in range(n):
            for i in range(n):
                if dist[i][k] == INF:
                    continue
                for j in range(n):
                    nd = dist[i][k] + dist[k][j]
                    if nd < dist[i][j]:
                        dist[i][j] = nd

        # Step 3: group originals by length
        by_len = {}
        for s in original:
            by_len.setdefault(len(s), set()).add(s)

        max_len = max(by_len.keys())

        m = len(source)
        dp = [INF] * (m + 1)
        dp[m] = 0

        # Step 4: DP
        for i in range(m - 1, -1, -1):
            # characters already match
            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            # try only valid lengths
            for L in by_len:
                if i + L > m:
                    continue

                s_sub = source[i:i + L]
                if s_sub not in by_len[L]:
                    continue

                t_sub = target[i:i + L]
                if t_sub not in idx:
                    continue

                c = dist[idx[s_sub]][idx[t_sub]]
                if c < INF:
                    dp[i] = min(dp[i], c + dp[i + L])

        return -1 if dp[0] == INF else dp[0]
