# Recursion - Live Coding Solutions

Speaker: Hiệp

## [1. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)

```java
class Solution {
    public int fib(int n) {
        if (n < 2) return n;
        return fib(n - 1) + fib(n - 2);
    }
}
```

Complexity:

- Time: O(2^n).
- Space: O(2^n).

```python
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

Complexity:

- Time: O(n).
- Space: O(n).

## [2. Power of Three](https://leetcode.com/problems/power-of-three/)

```java
class Solution {
    public boolean isPowerOfThree(int n) {
        // base case
        if (n <= 0) return false;
        if (n == 1) return true;
        if (n % 3 != 0) return false;
        // recursion
        return isPowerOfThree(n / 3);
    }
}
```

Complexity:

- Time: O(log n).
- Space: O(log n).

## [3. Happy Number](https://leetcode.com/problems/happy-number/description/)

```java
class Solution {

    Set<Integer> seen = new HashSet<>();

    private int sumOfSquaredDigits(int n) {
        // base case
        if (n < 10) return n * n;
        int lastDigit = n % 10;
        // recursion
        return sumOfSquaredDigits(n / 10) + lastDigit * lastDigit;
    }

    public boolean isHappy(int n) {
        // base case
        if (n == 1) return true;
        if (seen.contains(n)) return false;
        seen.add(n);

        // recursion
        return isHappy(sumOfSquaredDigits(n));
    }
}
```

Complexity:

- Time: O(log^2 n).
- Space: O(log n).