import java.math.BigInteger;

class Solution {
    public String addBinary(String a, String b) {
        BigInteger bA = new BigInteger(a, 2);
        BigInteger bB = new BigInteger(b, 2);
        BigInteger sum = bA;
        while (bB.compareTo(BigInteger.ZERO) != 0) {
            sum = bA.xor(bB);
            BigInteger carry = bA.and(bB).shiftLeft(1);
            bA = sum;
            bB = carry;
        }
        
        return sum.toString(2);
    }
}