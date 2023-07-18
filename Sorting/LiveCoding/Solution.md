## Find Target Indices After Sorting Array

Link problem: https://leetcode.com/problems/find-target-indices-after-sorting-array/

```
class Solution {
    // Time complexity: O(NlogN)
    // Space complexity: O(1)
    public List<Integer> targetIndices(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            if (nums[i] == target) {
                res.add(i);
            }
        }    
        return res;
    }
}
```

## How Many Numbers Are Smaller Than the Current Number
Link problem: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

```
class Solution {
    // Time complexity: O(NlogN)
    // Space complexity: O(N)
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int[][] tmp = new int[n][2];
        for (int i = 0; i < n; ++i) {
            tmp[i][0] = nums[i];
            tmp[i][1] = i;
        }
        Arrays.sort(tmp, (a,b) -> a[0] > b[0] ? 1 : -1);
        int[] res = new int[n];
        for (int i = 1; i < n; ++i) {
            if (tmp[i][0] != tmp[i-1][0]) {
                res[tmp[i][1]] = i;
            } else {
                res[tmp[i][1]] = res[tmp[i-1][1]];
            }
        }
        return res;
    }
}
```
## Sort the Students by Their Kth Score
Link problem: https://leetcode.com/problems/sort-the-students-by-their-kth-score/

```
class Solution {
    // Time complexity: O(MLogM) where M is the number of rows
    // Time complexity: O(1)
    public int[][] sortTheStudents(int[][] score, int k) {
        Arrays.sort(score, (a,b) -> a[k] > b[k] ? -1 : 1);
        return score;
    }
}
```


## Relative Sort Array
Link problem: https://leetcode.com/problems/relative-sort-array/description/

### Solution 1

```
class Solution {
    // Time complexity: O(N*M + NlogN) where N is arr1.length and M is arr2.length
    // Space complexity: O(1)
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int n = arr1.length;
        int m = arr2.length;
        Arrays.sort(arr1);
        int[] res = new int[n];
        int idx = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (arr1[j] == arr2[i]) {
                    res[idx++] = arr1[j];
                    arr1[j] = -1;
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            if (arr1[i] != -1) {
                res[idx++] = arr1[i];
            }
        }
        return res;
    }
}
```

### Solution 2

```
class Solution {
    // Time complexity: O(N + M)
    // Space complexity: O(1)
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int n = arr1.length;
        int m = arr2.length;
        int[] count = new int[1001];


        for (int num : arr1) {
            count[num]++;
        }
        int[] res = new int[n];
        int idx = 0;
        for (int num : arr2) {
            while (count[num] > 0) {
                res[idx++] = num;
                count[num]--;
            }
        }
        for (int i = 0; i < 1001; ++i) {
            while (count[i] > 0) {
                res[idx++] = i;
                count[i]--;
            }
        }
        return res;
    }
}
```






