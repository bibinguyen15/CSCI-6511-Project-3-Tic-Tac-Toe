import time
from API import createGame, getBoardString, getMove, makeMove
from constants import user, boardSize, target
from minimax import nextMove
from tictactoe import Board

def intialLoadGame(gameId, teamId2, firstMove=True):
    flag = True
    if gameId == 0:
        gameId = createGame(gameId, teamId2, boardSize, target)
        print(gameId)
        time.sleep(5)
        madeMove = False
    else:
        madeMove = True
    boardDetails = getBoardString(gameId)
    print(boardDetails)
    board = Board(boardDetails["target"], boardDetails["target"], 0)
    if firstMove:
        positionX = positionY = board.getSize() //2
        if madeMove:
            jsonData = getBoardString(gameId)
            while jsonData['code'] == 'FAIL':
                time.sleep(1)
                print("Move has been made")
            time.sleep(1)
            userMove = getMove(gameId, 1)
            x, y = userMove['x'], userMove['y']
            board.add((x, y), 0)
            if x == positionX and y == positionY:
                positionY += 1
        while firstMove:
            move = makeMove((positionX, positionY), gameId)
            if move["code"] == "OK":
                firstMove = False
                board.add((positionX, positionY), 1)
                print(board.board)
    
    while flag:
        time.sleep(2)
        userMove = getMove(gameId, 1)
        # print(userMove)
        moveX, moveY = userMove["x"], userMove["y"]
        while moveX == positionX and moveY == positionY:
            time.sleep(2)
            userMove = getMove(gameId, 1)
            moveX, moveY = userMove["x"], userMove["y"]
        x, y = userMove["x"], userMove["y"]
        board.add((x, y), 0)
        print(board.board)
        moveMade = localPlay(gameId)
        time.sleep(2)
        if moveMade["code"] == "FAIL":
            time.sleep(2)
        else:
            board.add(([moveMade[0], moveMade[1]]), 1)
            board.gameOver()
            print("our move:")
            print(board.board)
            userMove = getMove(gameId, 1)
            moveX, moveY = userMove["x"], userMove["y"]
            while moveX == moveMade[0] and moveY == moveMade[1]:
                time.sleep(2)
                userMove = getMove(gameId, 1)
                moveX, moveY = userMove["x"], userMove["y"]
            x, y = userMove["x"], userMove["y"]
            board.add((x, y), 0)
            print("opponent move:")
            print(board.board)



def localPlay(gameId):
    game = Board(boardSize, target, user)
    game.drawBoard()

    # while(True):
    #     player = int(input("Player's turn: "))
    #     if game.getUser() != player:
    #         game.switchUser(player)

    #     start = time.time()
    move = nextMove(game, 0)

        # game.add(nextMove(game, player), player)

        # end = time.time()

        # game.drawBoard()
        # print("Time taken", end - start, "s")
        # print("__________________________________________________________________")

        # if game.isFull():
        #     print("It's a draw.")
        #     break
        # elif game.gameOver():
        #     print("Winner:", end=" ")
        #     if game.getWinner() == 1:
        #         print(game.getPlayer(player))
        #     else:
        #         print(game.getPlayer(player - 1))
        #     break
    return makeMove(move, gameId)

