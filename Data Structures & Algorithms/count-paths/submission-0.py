class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n
        dp_grid = [row.copy() for _ in range(m)]

        if m == 1 or n == 1:
            return 1

        dp_grid[0][0] = 1

        for y_val in range(m):
            for x_val in range(n):
                if y_val == 0 and x_val == 0:
                    continue

                left = (y_val, x_val - 1)
                bottom = (y_val - 1, x_val)

                neighbors = (left, bottom)
                cur_sum = 0

                for coord in neighbors:
                    if (coord[0] >= 0 and coord[0] < m
                            and coord[1] >= 0 and coord[1] < n):
                        cur_sum += dp_grid[coord[0]][coord[1]]

                dp_grid[y_val][x_val] = cur_sum

        return dp_grid[m - 1][n - 1]