/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if (n == 1) {
            return isBadVersion(1) ? 1 : 0;
        }
        int left = 1;
        int right = n;
        int pos = 0;
        while (left < right) {
            pos = left/2 + right/2;
            if (isBadVersion(pos)) {
                right = pos;
            } else {
                left = pos + 1;
            }
        }
        
        return left;
    }
}