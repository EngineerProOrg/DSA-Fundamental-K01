// https://leetcode.com/problems/find-pivot-index/description/

class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0, n = nums.length;
        for (int i = 0; i < n; ++i) sum += nums[i];

        int left = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == sum - 2*left) return i;
            left += nums[i];
        }
        return -1;
    }
}