class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # We go in two pointers from both sides of the list
        # We have the following cases:
        # xi + xj > N: we decrease j
        # xi + xj < N: we increase i
        # xi + xj = N => return [x1+1, x2+1]
        i,j = 0, len(numbers) - 1
        while i < j:
            summa = numbers[i] + numbers[j]
            if summa > target:
                j -= 1
            elif summa < target:
                i += 1
            else:
                return [i+1, j+1]