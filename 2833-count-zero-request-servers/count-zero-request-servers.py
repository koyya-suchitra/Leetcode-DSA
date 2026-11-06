from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        ordered_queries = sorted(enumerate(queries), key=lambda item: item[1])
        counts = [0] * (n + 1)
        active = 0
        left = right = 0
        answer = [0] * len(queries)

        for index, end in ordered_queries:
            while right < len(logs) and logs[right][1] <= end:
                server = logs[right][0]
                if counts[server] == 0:
                    active += 1
                counts[server] += 1
                right += 1

            start = end - x
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    active -= 1
                left += 1

            answer[index] = n - active

        return answer