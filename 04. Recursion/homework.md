# Recursion - Homework Solutions

Speaker: Hiệp

## [1. Power of Four](https://leetcode.com/problems/power-of-four/)

```java
class Solution {
    public boolean isPowerOfFour(int n) {
        if (n <= 0) return false;
        if (n == 1) return true;
        return n % 4 == 0 && isPowerOfFour(n / 4);
    }
}
```

Complexity:

- Time: O(log n).
- Space: O(log n).

## [2. Sum of Digits in Base K](https://leetcode.com/problems/sum-of-digits-in-base-k/description/)

```java
class Solution {
    public int sumBase(int n, int k) {
        if (n == 0) return 0;
        int lastDigit = n % k;
        return lastDigit + sumBase(n / k, k);
    }
}
```

Complexity:

- Time: O(log n).
- Space: O(log n).

## [3. Base 7](https://leetcode.com/problems/base-7/description/)

```java
class Solution {
    public String convertToBase7(int num) {
        if (num < 0) return "-" + convertToBase7(-num);
        if (num < 7) return "" + (char) ('0' + num);
        return convertToBase7(num / 7) + (char) ('0' + num % 7);
    }
}
```

Complexity:

- Time: O(log n).
- Space: O(log n).

## [4. Tower of Hanoi](https://www.lintcode.com/problem/169/)

```java
public class Solution {

    List<String> res;

    private void solve(int n, String from, String to, String mid) {
        if (n == 1) {
            res.add(String.format("from %s to %s", from, to));
            return;
        }
        solve(n - 1, from, mid, to);
        res.add(String.format("from %s to %s", from, to));
        solve(n - 1, mid, to, from);
    }

    /**
     * @param n: the number of disks
     * @return: the order of moves
     */
    public List<String> towerOfHanoi(int n) {
        res = new ArrayList<>();
        solve(n, "A", "C", "B");
        return res;
    }
}
```

Complexity:

- Time: O(2^n).
- Space: O(2^n).