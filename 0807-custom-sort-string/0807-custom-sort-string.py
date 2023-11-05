class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #counts = collections.Counter(s)
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        res = []
        for c in order:
            res += [c] * counts[c]
            counts[c] = 0
        for c in [c for c in counts if counts[c] != 0]:
            res += [c] * counts[c]

        return "".join(res)