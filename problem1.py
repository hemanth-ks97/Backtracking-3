# Time Complexity : O(n!)
# Space Complexity : O(n^2)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur_solution = []
        for i in range(n):
            cur_solution.append(["."] * n)
        
        col_set = set()
        diag1_set = set()
        diag2_set = set()

        def isValid(r,c):
            if c in col_set or r+c in diag1_set or r-c in diag2_set:
                return False
            return True
        
        def recurse(r):
            #base
            if r == n:
                sol = []
                for row in cur_solution:
                    row_str = ""
                    for c in row:
                        row_str += c
                    sol.append(row_str)
                res.append(sol)
            #logic
            for c in range(n):
                if isValid(r,c):
                    cur_solution[r][c] = 'Q'
                    col_set.add(c)
                    diag1_set.add(r+c)
                    diag2_set.add(r-c)
                    recurse(r + 1)
                    cur_solution[r][c] = "."
                    col_set.remove(c)
                    diag1_set.remove(r+c)
                    diag2_set.remove(r-c)
        
        recurse(0)
        return res
