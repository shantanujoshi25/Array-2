# // Time Complexity : O(n)
# // Space Complexity : O( 1)
    
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # if 0 -> 1 then replace with 2
        # if 1 -> 0 then replace with 3
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                neighbors = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                live_neigh = 0
                cell = board[i][j]
                
                for n in neighbors:
                    if((n[0]>=0 and n[0]<len(board)) and (n[1]>=0 and n[1]<len(board[0]))):
                        if(board[n[0]][n[1]] == 1 or board[n[0]][n[1]] == 3):
                            live_neigh += 1
                
                if(cell and (live_neigh < 2)):
                    board[i][j] = 3
                elif(cell and (live_neigh == 2 or live_neigh == 3)):
                    pass
                elif(cell and (live_neigh > 3)):
                    board[i][j] = 3
                elif(cell == 0 and (live_neigh == 3)):
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 2):
                    board[i][j] = 1
                elif(board[i][j] == 3):
                    board[i][j] = 0
                
