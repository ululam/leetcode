class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        var totalSum = 0;

        for (int i=0; i< arr.length; i++) {
            totalSum += arr[i];
        }

        // If we have 3 subarrays with equal sum != 0, that means:
        // - sum of all element is dividable by 3
        // - subarray sum = all_elements_sum / 3
        if (totalSum % 3 != 0) {
            return false;
        }

        final var subarrSum = totalSum / 3;

        int sum = 0;
        int count = 0;
        for (int i=0; i< arr.length; i++) {
            sum += arr[i];
            if (sum == subarrSum && count < 3) {
                count++;
                sum = 0;
            }
        }

        return count == 3 && sum == 0;
    }
}