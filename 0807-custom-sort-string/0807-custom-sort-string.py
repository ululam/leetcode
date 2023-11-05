class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #counts = collections.Counter(s)
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        res = []
        for c in order:
            res += [c] * counts[c]
            del counts[c]
        for c in counts:
            # Zeros counted chars are auto-filtered here
            res += [c] * counts[c]

        return "".join(res)