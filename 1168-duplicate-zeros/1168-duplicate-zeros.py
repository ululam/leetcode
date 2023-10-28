class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)-1
        zeroCount = 0

        for i in range(n+1):
            if i > n - zeroCount:
                break
            if arr[i] == 0:
                # Edge case: last 0
                if i == n - zeroCount:
                    arr[n] = 0
                    n -= 1
                    break
                zeroCount += 1

        start = n - zeroCount
        for i in range(start, -1, -1):
            arr[i + zeroCount] = arr[i]
            if arr[i] == 0:
                zeroCount -= 1
                arr[i + zeroCount] = 0