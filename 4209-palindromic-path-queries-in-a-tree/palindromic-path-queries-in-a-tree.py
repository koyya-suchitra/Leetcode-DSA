
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        from collections import defaultdict

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n

        chars = list(s)
        timer = 0

        # Euler tour, binary lifting table, and initial root-prefix masks
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1

                parent[0][u] = u if p == -1 else p
                for j in range(1, LOG):
                    parent[j][u] = parent[j - 1][parent[j - 1][u]]

                bit = 1 << (ord(chars[u]) - ord('a'))
                prefix[u] = bit ^ (prefix[p] if p != -1 else 0)

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # LCA using binary lifting
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        # Fenwick tree supporting range XOR updates and point queries
        bit_tree = [0] * (n + 2)

        def update(i, value):
            while i <= n:
                bit_tree[i] ^= value
                i += i & -i

        def range_xor(left, right, value):
            update(left + 1, value)
            update(right + 2, value)

        def point_query(i):
            result = 0
            i += 1
            while i > 0:
                result ^= bit_tree[i]
                i -= i & -i
            return result

        def current_prefix(u):
            return prefix[u] ^ point_query(tin[u])

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_bit = 1 << (ord(chars[u]) - ord('a'))
                new_bit = 1 << (ord(c) - ord('a'))
                delta = old_bit ^ new_bit

                if delta:
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)
                mask = (
                    current_prefix(u)
                    ^ current_prefix(v)
                    ^ (1 << (ord(chars[w]) - ord('a')))
                )

                # At most one character can have an odd frequency.
                answer.append((mask & (mask - 1)) == 0)

        return answer
