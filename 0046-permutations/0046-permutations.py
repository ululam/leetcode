class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.permuteDfs(nums)
        # return self.permuteBackTrack(nums)

    def permuteBackTrack(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(nums) == len(curr):
                res.append(curr[:])
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()
        res = []
        backtrack([])
        return res

# ---------------

    def permuteDfs(self, nums: List[int]) -> List[List[int]]:
        return self.doPermute(None, nums)

    def doPermute(self, number, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[number]] if number else [[]]
        perms = self.doPermute(nums[0], nums[1:])
        return self.permuteSub(number, perms) if number is not None else perms

        
    def permuteSub(self, number, subnums: List[List[int]]) -> List[List[int]]:
        res = []
        for lst in subnums:
            res += self.permute1(number, lst)
        return res
    
    def permute1(self, number, lst):
        res = []
        for i in range(len(lst)+1):
            newList = lst[:]
            newList.insert(i, number)
            res.append(newList)
        return res
