class Solution(object):
    ONE_DIGIT = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

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
        billions = intNum / 1000000000
        # here we know that its not more than 4
        numStr += "" if billions == 0 else self.getStrRepresentation(billions, "Billion")
        
        millions = (intNum - billions * 1000000000) / 1000000
        numStr += "" if millions == 0 else " " + self.getStrRepresentation(millions, "Million")

        thousands = (intNum - billions * 1000000000 - millions * 1000000) / 1000
        numStr += "" if thousands == 0 else " " + self.getStrRepresentation(thousands, "Thousand")

        leftOver = intNum - billions * 1000000000 - millions * 1000000 - thousands * 1000
        numStr += "" if leftOver == 0 else " " + self.getStrRepresentation(leftOver, "")
        
        return numStr.strip()

    def fromTwentyToNinety(self, num):
        decims = num / 10
        leftOVer = num - decims * 10
        leftOVer = "" if leftOVer == 0 else " " + self.fromOneToNine(leftOVer)
        if decims == 2:
            return "Twenty" + leftOVer
        if decims == 3:
            return "Thirty" + leftOVer
        if decims == 4:
            return "Forty" + leftOVer
        if decims == 5:
            return "Fifty" + leftOVer
        if decims == 6:
            return "Sixty" + leftOVer
        if decims == 7:
            return "Seventy" + leftOVer
        if decims == 8:
            return "Eighty" + leftOVer
        if decims == 9:
            return "Ninety" + leftOVer    
        raise Exception("Number beyond range: " + str(num))

    def fromTenToNineteen(self, num):
        if num == 10:
            return "Ten"
        if num == 11:
            return "Eleven"
        if num == 12:
            return "Twelve"
        if num == 13:
            return "Thirteen"
        if num == 14:
            return "Fourteen"
        if num == 15:
            return "Fifteen"
        if num == 16:
            return "Sixteen"
        if num == 17:
            return "Seventeen"
        if num == 18:
            return "Eighteen"
        if num == 19:
            return "Nineteen"
        raise Exception("Number beyond range: " + str(num))

    def fromOneToNine(self, num):
        return Solution.ONE_DIGIT[num-1]
        # raise Exception("Number beyond range: " + str(num))

    def fromOneToNineteen(self, num):
        return self.fromOneToNine(num) if num < 10 else self.fromTenToNineteen(num)

    def getStrRepresentation(self, numLess1000, name):
        numStr = ""
        if numLess1000 == 0:
            return numStr

        hundreds = numLess1000 / 100
        numStr += "" if hundreds == 0 else self.fromOneToNine(hundreds) + " " + self.getPlural(hundreds, "Hundred")
        leftOver = numLess1000 - hundreds * 100
        if leftOver > 0:
            numStr += " " if len(numStr) > 0 else ""
            numStr += self.fromOneToNineteen(leftOver) if leftOver < 20 else self.fromTwentyToNinety(leftOver)

        if name == "":
            return numStr


        return numStr + " " + self.getPlural(numLess1000, name)

    def getPlural(self, num, str):
        return str
        # if num == 1:
        #     return str
        # return str + "s"