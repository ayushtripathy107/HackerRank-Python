class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # If we've matched all characters in 'word'
            if i == len(word):
                return True
            
            # Boundary checks and character mismatch
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False
            
            # Add current cell to path and explore neighbors
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack: remove cell from path
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
