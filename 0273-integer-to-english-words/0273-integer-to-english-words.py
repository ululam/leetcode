class Solution(object):
    ONE_DIGIT = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    TEEN = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    TIES = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    DIVIDERS = {1000000000: "Billion", 1000000: "Million", 1000: "Thousand"}

    def numberToWords(self, num):
        # max int = 4_294_967_296
        # 1. Transfer num to int
        # 2. Use pattern "[A billion(s) ][B million(s) ][C thousand(s) ][D hundred(s) ][several cases]"
        # 3. Each number is % 10^[9,6,3]
        # 4. Then we have a function to convert 3-digit value into string, for each 10^3:
        #   a. [X hundrded][tail]
        # 5. tail
        #   a. E < 20? -> use switch: 1..19 -> string
        #   b. Else [% 10] -> switch: 1..9 -> string
        #   => two functions: lessTwenty(), fromTwentyToNinety()
        intNum = int(num)
        if intNum == 0:
            return "Zero"

        numStr = ""
        for div, name in Solution.DIVIDERS.items():
            ions = intNum // div
            if (ions > 0):
                numStr = self.addPart(numStr, self.fromHundreds(ions, name))
                intNum -= ions * div                

        if intNum > 0:
            numStr = self.addPart(numStr, self.fromHundreds(intNum, ""))
        
        return numStr #.strip()

    def fromTwentyToNinety(self, num):
        decims = num // 10   # We know its > 0
        leftOVer = num - decims * 10
        leftOVer = "" if leftOVer == 0 else " " + self.fromOneToNine(leftOVer)
        return Solution.TIES[decims-2] + leftOVer

    def fromTenToNineteen(self, num):
        return Solution.TEEN[num-10]

    def fromOneToNine(self, num):
        return Solution.ONE_DIGIT[num-1]

    def fromOneToNineteen(self, num):
        return self.fromOneToNine(num) if num < 10 else self.fromTenToNineteen(num)

    def fromHundreds(self, numLess1000, name):
        if numLess1000 == 0:
            return ""

        hundreds = numLess1000 // 100
        result = ""
        if hundreds > 0:
            result = self.fromOneToNine(hundreds) + " Hundred"

        leftOver = numLess1000 - hundreds * 100
        if leftOver > 0:
            addOn = self.fromOneToNineteen(leftOver) if leftOver < 20 else self.fromTwentyToNinety(leftOver)
            result = self.addPart(result, addOn)
        
        return result if len(name) == 0 else result + " " + name 

    def addPart(self, prevStr, text):
        return text if len(prevStr) == 0 else prevStr + " " + text