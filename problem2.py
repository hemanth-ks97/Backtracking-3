# Time Complexity : O(n*m*3^L) L -> length of word
# Space Complexity : O(L)
# Did this code successfully run on Leetcode : YES

# Any problem you faced while coding this : NO
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board), len(board[0])
        if len(word) > R*C:
            return False
        
        visited = set()
        def isValid(r,c):
            return 0 <= r < R and 0 <= c <C
            
        def dfs(node, ix):
            # base
            if ix == len(word)-1:
                return True
            # logic
            visited.add(node)
            r,c = node
            for di,dj in [[0,1],[0,-1],[-1,0],[1,0]]:
                dr,dc = r+di, c+dj
                if isValid(dr,dc) and (dr,dc) not in visited and board[dr][dc] == word[ix + 1]:
                    if dfs((dr,dc), ix+1):
                        return True
            # backtrack
            visited.remove(node)
            return False

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    if dfs((i,j), 0):
                        return True
        
        return False
