# Array - Homework Solutions

Speaker: Hiệp

## [1. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)

```java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int x: nums) {
            int id = Math.abs(x) - 1;
            nums[id] = -Math.abs(nums[id]);
        }
        List<Integer> res = new ArrayList<>();
        for  (int i = 1; i <= nums.length; ++i) {
            if (nums[i - 1] > 0) res.add(i);
        }
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(1).

## [2. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

```java
class NumArray {

    int[] sum;

    public NumArray(int[] nums) {
        int n = nums.length;
        sum = new int[n + 1];
        for (int i = 1; i <= n; ++i) sum[i] = sum[i - 1] + nums[i - 1];
    }
    
    public int sumRange(int left, int right) {
        return sum[right + 1] - sum[left];
    }
}
```

Complexity:

- Time: init: O(n), query: O(1).
- Space: O(n).

## [3. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/)

```java
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int cnt = 0, m = flowerbed.length;
        for (int i = 0; i < m; ++i) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == m - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                cnt++;
            }
        }
        return cnt >= n;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(1).

## [4. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        res[n - 1] = 1;
        for (int i = n - 2; i >= 0; --i) res[i] = nums[i + 1] * res[i + 1];
        int prod = 1;
        for (int i = 0; i < n; ++i) {
            res[i] *= prod;
            prod *= nums[i];
        }
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(1).

## [5. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0, n = prices.length, buy = prices[0];
        for (int i = 1; i < n; ++i) {
            if (prices[i] > buy) res += prices[i] - buy;
            buy = prices[i];
        }
        return res;
    }
}
```

Complexity:

- Time: O(n).
- Space: O(1).

## [6. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] row = new boolean[9][9];
        boolean[][] col = new boolean[9][9];
        boolean[][] box = new boolean[9][9];

        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') continue;
                int x = board[i][j] - '1';
                if (row[i][x] || col[j][x] || box[(i / 3) * 3 + j / 3][x]) return false;
                row[i][x] = col[j][x] = box[(i / 3) * 3 + j / 3][x] = true;
            }
        }
        return true;
    }
}
```

Complexity:

- Time: O(1).
- Space: O(1).