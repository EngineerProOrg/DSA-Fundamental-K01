## Keys and Rooms

Link problem: https://leetcode.com/problems/keys-and-rooms/description/

```
class Solution {
    // Time complexity: O(N + M) where N is number of nodes and M is number of edges
    // Space complexity: O(N)
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        boolean[] vis = new boolean[n];
        dfs(0, rooms, vis);
        for (boolean v : vis) {
            if (!v) {
                return false;
            }
        }
        return true;
    }


    private void dfs(int room, List<List<Integer>> rooms, boolean[] vis) {
        // room =
        vis[room] = true;
        for (int nextRoom : rooms.get(room)) { // nextRoom:
            if (vis[nextRoom]) {
                continue;
            }
            dfs(nextRoom, rooms, vis);
        }
    }
}
```

## Number of Provinces

Link problem: https://leetcode.com/problems/number-of-provinces

```
class Solution {
    // Time complexity: O(N^2)
    // Space complexity: O(N)
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] vis = new boolean[n];
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (vis[i]) {
                continue;
            }
            res++;
            dfs(i, n, vis, isConnected);
        }
        return res;
    }


    private void dfs(int cur, int n, boolean[] vis, int[][] isConnected) {
        vis[cur] = true;
        for (int i = 0; i < n; ++i) {
            if (vis[i] || isConnected[cur][i] == 0) {
                continue;
            }
            dfs(i, n, vis, isConnected);
        }
    }
}

```

## Find Eventual Safe States

Link problem: https://leetcode.com/problems/find-eventual-safe-states/


```
class Solution {
    // Time complexity: O(N + M) where N is number of nodes and M is number of edges
    // Space complexity: O(N)
    int n;


    public List<Integer> eventualSafeNodes(int[][] graph) {
        n = graph.length;    
        boolean[] vis = new boolean[n];
        boolean[] path = new boolean[n];


        for (int i = 0; i < n; ++i) {
            if (vis[i]) {
                continue;
            }
            dfs(i, vis, path, graph);
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; ++i) {
            if (!path[i]) {
                res.add(i);
            }
        }
        return res;
    }


    private boolean dfs(int cur, boolean[] vis, boolean[] path, int[][] graph) {
        vis[cur] = true;
        path[cur] = true;
        for (int u : graph[cur]) {
            if (!vis[u]) {
                if (!dfs(u, vis, path, graph)) {
                    return false;
                }
            } else if (path[u]) {
                return false;
            }
        }
        path[cur] = false;
        return true;
    }
}

```

## Is Graph Bipartite?

Link problem: https://leetcode.com/problems/is-graph-bipartite/

```
class Solution {
    // Time complexity: O(N + M)
    // Space complexity: O(M)
    int n;
    public boolean isBipartite(int[][] graph) {
        n = graph.length;
        int[] colors = new int[n];
        boolean[] vis = new boolean[n];
        for (int i = 0; i < n; ++i) {
            if (colors[i] != 0) continue;
            if (!dfs(i, vis, colors, graph, 1)) {
                return false;
            }
        }
        return true;
    }


    private boolean dfs(int cur, boolean[] vis, int[] colors, int[][] graph, int color) {
        if (colors[cur] == 0) {
            colors[cur] = color;
        } else if (colors[cur] != color) {
            return false;
        }
        vis[cur] = true;


        int[] cons = graph[cur];
        int nextColor = color == 1 ? 2 : 1;
        for (int u : graph[cur]) {  
            if (!vis[u]) {
                if (!dfs(u, vis, colors, graph, nextColor)) {
                    return false;
                }
            }
            if (colors[u] != nextColor) {
                return false;
            }          
           
        }
        return true;
    }
}
```
