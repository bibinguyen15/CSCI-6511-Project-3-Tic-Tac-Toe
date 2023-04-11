class TTT:
    def __init__(self, boardSize, target):
        self.boardSize = boardSize
        self.target = target
        self.players = ['O', 'X']
        print(self.players[1])
        self.board = [['-'] * boardSize] * boardSize
        self.available = []
        for x in range(boardSize):
            for y in range(boardSize):
                self.available.append([x, y])
        print(self.available)

    def drawBoard(self):
        for row in self.board:
            print("|", end="")
            for i in row:
                print(i, end="|")
            print()
        print(self.boardSize, self.target)

    def setBoard(self, board, target=-1):
        self.board = board.split('\n')[:-1]
        for i in range(len(self.board)):
            self.board[i] = [*self.board[i]]
        print(self.board)
        self.boardSize = len(self.board)
        if target == -1:
            self.target = int(self.boardSize / 2)
        else:
            self.target = target

    def heu(self):
         for i in range(self.boardSize):
             if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                  if board[i][0] == self.players[1]:
                       return 10
                  elif board[i][0] == self.players[0]:
                       return -10
        
        # Check diagonal
         for i in range(self.boardSize):
              for j in range(self.boardSize + 1 - self.target):
                   if (i + self.target) <= self.boardSize:
                    value = [self.board[i + k][j + k]
                                 for k in range(self.target)]
                    if all(elem == value[0] for elem in value) and value[0] != '-':
                            return value[0]
                    elif(i - self.target + 1) >= 0:
                        value = [self.board[i - k][j + k]
                                 for k in range(self.target)]

                        if all(elem == value[0] for elem in value) and value[0] != '-':
                            return value[0]
    
    def min_max(self, board, depth, nodeIndex, isMax, player, alpha, beta) :  
        if (isMax):
            best = float('-inf')
            for i in range(self.boardSize):
                        for j in range(self.boardSize):
                             if (board[i][j]=='-') :
                                  board[i][j] = self.players[player]
                                  best = max(best, self.min_max(board,
											depth + 1, nodeIndex*2 +i,
											not isMax, player, alpha, beta))
                                  alpha = max(alpha, best)
                                  board[i][j] = '-'
                                  if beta <= alpha:
                                       #Alpha-Beta Pruning
                                       break
            return best
        
        else :
            best = float('inf')
            for i in range(self.boardSize):
                        for j in range(self.boardSize):
                            if (board[i][j] == '-') :
                                 board[i][j] = self.players[player]
                                 best = min(best, self.min_max(board, depth + 1, nodeIndex*2 + i, not isMax, player, alpha, beta))
                                 beta = min(beta, best)
                                 board[i][j] = '-'
                                 if beta <= alpha:
                                      #Alpha-Beta Pruning
                                      break
            return best
    
    def next(self, player):
        bestVal = float('-inf')
        bestMove = (-1, -1)
        for i in range(self.boardSize):
                    for j in range(self.boardSize):
                         if (self.board[i][j] == '-') :
                              self.board[i][j] = self.players[player]
                              moveVal = self.min_max(self.board, 0, 0, False, player, float('-inf'), float('inf'))
                            #   self.board[i][j] = '-'
                              if (moveVal > bestVal) :
                                   bestMove = (i, j)
                                   bestVal = moveVal
        print("The value of the best Move is :", bestMove)
        return bestMove

    def win(self):
        winner = ''
        adjacent = [self.board[0][0], 0]
        
        
        #First check row
        for row in self.board:
            adjacent = [row[0], 0]
            for item in row:
                #if match
                if item == adjacent[0] and item != '-':
                    adjacent[1] += 1
                    # print(adjacent)
                    if adjacent[1] == self.target:
                        return item
                else:
                    adjacent = [item, 1]
                    
                    
        #Check column
        for j in range(self.boardSize):
            adjacent = [self.board[0][j], 0]
            for i in range(self.boardSize):
                if self.board[i][j] == adjacent[0] and self.board[i][j] != '-':
                    adjacent[1] += 1
                    if adjacent[1] == self.target:
                        return self.board[i][j]
                else:
                    adjacent = [self.board[i][j], 1]
        
        #Check diagonal
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                adjacent = []
                
                
        #Check tie
        if len(self.available) == 0:
            return True
               
                    
def main():
    game = TTT(4, 4)

    game.setBoard("XXOX\n-OO-\n--O-\n----\n", 4)
    # game.setBoard("O-----------\nOO----------\n---O--------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n------------\n")
    game.drawBoard()
    game.next(1)
    print("Winner is:", game.win())


if __name__ == '__main__':
    main()
