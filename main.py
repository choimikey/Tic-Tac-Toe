import random

board = [" " for x in range(10)]

def pick(letter, pos):
    board[pos] = letter


def isEmpty(pos):
    return board[pos] == ' '


def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (
        bo[4] == le and bo[5] == le
        and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (
            bo[1] == le and bo[4] == le and
            bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (
                bo[3] == le and bo[6] == le
                and bo[9] == le) or (bo[1] == le and bo[5] == le
                                     and bo[9] == le) or (bo[3] == le
                                                          and bo[5] == le
                                                          and bo[7] == le)


def manMove():
    run = True
    while run:
        move = input('you\'re X. Enter your position: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isEmpty(move):
                    run = False
                    pick('X', move)
                else:
                    print('this space is ocupied')
        except:
            print("invalid position. try again ")


def compMove():
    # list all posible move for computer
    posibleMove = [
        index for index, value in enumerate(board)
        if index != 0 and value == ' '
    ]
    move = 0

    # to check winning posibilities,let stand for letter
    for let in ['O', 'X']:
        for i in posibleMove:
            #create a copy version of board
            copy_board = board[:]
            copy_board[i] = let
            if isWinner(copy_board, let):
                move = i
                return move

    connersOpen = []
    for i in posibleMove:
        if i in [1, 3, 7, 9]:
            connersOpen.append(i)

    if 5 in posibleMove:
        move = 5
        return move

    if len(connersOpen) > 0:
        move = selectRandom(connersOpen)
        return move

    edgesOpen = []

    for i in posibleMove:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(select_list):
    length = len(select_list)
    choice = random.randrange(0, length)
    return select_list[choice]


def IsFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("welcome to tic-tac-toe")
    printBoard(board)

    while not (IsFull(board)):
        # o won
        if not (isWinner(board, "O")):
            manMove()
            printBoard(board)
        else:
            print("you lose. better luck next time !!!")
            break

        # x win
        if not (isWinner(board, "X")):
            move = compMove()
            if move != 0:
                pick('O', move)
                print('\n')
                printBoard(board)
        else:
            print("you won !!!")
            break

    if IsFull(board):
        print("GGWP. tie game. what a game ")


main()
