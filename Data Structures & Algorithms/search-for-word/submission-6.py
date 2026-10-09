class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = set()

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i,j,k):
            #once you explored say (i,j) you need to pop this from the visited because
            #other node can visit this node 
            self.visited.add((i,j))

            if k == len(word):
                return True
            # add to visit set
            if (i,j) in self.visited or i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] != word[k]:
                return 
            else:
                dfs(i-1,j,k+1)
                dfs(i+1,j,k+1)
                dfs(i,j-1,k+1)
                dfs(i,j+1,k+1)
            self.visited.remove((i,j))


            # wanna keep going or break?

            # keep exploring
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        
        return False