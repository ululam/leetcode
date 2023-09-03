class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        iF = iS = 0
        
        res = []
        first = second = None

        while iF < len(firstList) and iS < len(secondList):
            first = firstList[iF] if not first else first
            second = secondList[iS]  if not second else second
            if first[1] < second[0]:
                first = None
                iF += 1
            elif second[1] < first[0]:
                second = None
                iS += 1
            else:
                startIndex = max(first[0], second[0])
                endIndex = min(first[1], second[1])
                res += [[startIndex, endIndex]]
                if first[1] > second[1]:
                    first = [endIndex, first[1]]
                    iS += 1
                    second = None
                else:
                    second = [endIndex, second[1]]
                    iF += 1
                    first = None

        return res

                

        