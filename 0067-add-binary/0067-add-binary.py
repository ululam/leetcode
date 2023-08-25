class Solution(object):
    def addBinary(self, a, b):
        # Starting from the last index of the strings, iterate back
        # Get 2 chars, "sum" them, storing result in a new array
        # Have a third char "transfer"
        # when one of the string ends, consider 2nd string c = 0
        # and return string from the resulting array (prefixed with transfer if == 1)
        bigS = a if len(a) > len(b) else b
        smallS = b if bigS == a else a
        delta = len(bigS) - len(smallS)
        transfer = 0
        res = ""
        for i in range (len(bigS)-1, -1, -1):
            print("i = " + str(i))
            c1 = int(bigS[i])
            c2 = int(smallS[i-delta]) if i-delta >= 0 else 0
            print(str(c1) + ", " + str(c2))
            summ = c1 + c2 + transfer
            if summ == 0:
                res = '0' + res
                transfer = 0                
            elif summ == 1:
                res = '1' + res
                transfer = 0
            elif summ == 2:
                res = '0' + res
                transfer = 1
            else:
                res = '1' + res
                transfer = 1

        return res if transfer == 0 else '1'+res
            



