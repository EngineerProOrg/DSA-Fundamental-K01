# Array - Live Coding Solutions

Speaker: Hiệp

## [1. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int result = 0;
        int minPrice = prices[0];
        for (int j = 1; j < n; ++j) {
            result = Math.max(result, prices[j] - minPrice);
            minPrice = Math.min(minPrice, prices[j]);
        }
        return result;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(1).

## [2. Remove Element](https://leetcode.com/problems/remove-element/description/)

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int cnt = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != val) {
                nums[cnt] = nums[i];
                cnt++;
            }
        }
        return cnt;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(1).

## [3. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

```java
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < numRows; ++i) {
            List<Integer> row = new ArrayList<>();
            row.add(1);
            for (int j = 1; j < i; ++j) {
                row.add(arr.get(i - 1).get(j - 1) + arr.get(i - 1).get(j));
            }
            if (i > 0) {
                row.add(1);
            }
            arr.add(row);
        }
        return arr;
    }
}
```

Complexity:

- Time: O(numRows^2).
- Space: O(numRows^2).

## [4. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)
```java
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
```

Complexity:

- Time: O(n).
- Space: O(1).