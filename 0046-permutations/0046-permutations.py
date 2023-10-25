class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        if not lst:
            return [[number]]
        res = []
        for i in range(len(lst)+1):
            newList = lst[:]
            newList.insert(i, number)
            res.append(newList)
        return res
