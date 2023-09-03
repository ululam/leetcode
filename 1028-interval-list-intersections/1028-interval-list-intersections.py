class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        iF = iS = 0
        
        res = []
        first = second = None

        while iF < len(firstList) and iS < len(secondList):
            first = firstList[iF]
            second = secondList[iS]
            if first[1] < second[0]:
                iF += 1
            elif second[1] < first[0]:
                iS += 1
            else:
                startIndex = max(first[0], second[0])
                endIndex = min(first[1], second[1])
                res += [[startIndex, endIndex]]
                if first[1] > second[1]:
                    iS += 1
                else:
                    iF += 1

        return res

                

        