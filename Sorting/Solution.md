##  Height Checker
https://leetcode.com/problems/height-checker/description/
```
class Solution {
    // Time complexity: O(NlogN)
    // Space complexity: O(N)
    public int heightChecker(int[] heights) {
        int n = heights.length;
        int[] copy = heights.clone();
        Arrays.sort(copy);
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (copy[i] != heights[i]) {
                res++;
            }
        }
        return res;
    }
}
```


## Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

### Solution 1
```
class Solution {
    // Time complexity: O(m+n)
    // Space complexity: O(m)
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] tmp1 = new int[m];
        for (int i = 0; i < m; ++i) {
            tmp1[i] = nums1[i];
        }
        int p1 = 0;
        int p2 = 0;
        int idx = 0;
        while (p1 < m && p2 < n) {
            if (tmp1[p1] <= nums2[p2]) {
                nums1[idx++] = tmp1[p1++];
            } else {
                nums1[idx++] = nums2[p2++];
            }
        }
        for (; p1 < m; ++p1) {
            nums1[idx++] = tmp1[p1];
        }
        for (; p2 < n; ++p2) {
            nums1[idx++] = nums2[p2];
        }
    }
}
```

### Solution 2
Merge in-place without a temp array
```
class Solution {
    // Time complexity: O(m+n)
    // Space complexity: O(1)
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int len = m + n;
        int p1 = m-1;
        int p2 = n-1;
        int idx = len-1;
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] >= nums2[p2]) {
                nums1[idx] = nums1[p1--];
            } else {
                nums1[idx] = nums2[p2--];
            }
            idx--;
        }
        for (; p1 >= 0; --p1) {
            nums1[idx--] = nums1[p1];
        }
        for (; p2 >= 0; --p2) {
            nums1[idx--] = nums2[p2];
        }
    }
}
```


## Minimum Cost of Buying Candies With Discount
https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

```
class Solution {
    // Time complexity: O(NlogN)
    // Space complexity: O(1)
    public int minimumCost(int[] cost) {
        int n = cost.length;
        int res = 0;
        Arrays.sort(cost);
        for (int i = n-1; i >= 0; --i) {
            res += cost[i];
            int secCost = i > 0 ? cost[i-1] : 0;
            res += secCost;
            i-=2;
        }
        return res;
    }
}
```

## Make Array Zero by Subtracting Equal Amounts
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

```
class Solution {
    // Time complexity: O(NlogN)
    // Space complexity: O(1)
    public int minimumOperations(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int sum = 0;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            nums[i]-=sum;
            if (nums[i] > 0) {
                res++;
            }
            sum += nums[i];
        }
        return res;
    }
}
```

## Widest Vertical Area Between Two Points Containing No Points
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

```
class Solution {
    // Time complexity: O(NlogN) where N is points.length
    // Space complexity: O(1)
    public int maxWidthOfVerticalArea(int[][] points) {
        int n = points.length;
        Arrays.sort(points, (a,b) -> a[0] > b[0] ? 1 : -1);
        int res = Integer.MIN_VALUE;


        for (int i = 1; i < n; ++i) {
            res = Math.max(res, points[i][0] - points[i-1][0]);
        }
        return res;
    }
}
```



