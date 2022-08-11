board_size=15
board=[]
def intboard():
    for i in range(board_size):
        row=['✚']*board_size
        board.append(row)
def printboard():
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j],end='')
        print()

#定义获胜方式，有六种方式，横、竖、左下斜、右下斜
def victory():
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j]=='●':
                if board[i][j+1]!='●':
                    if board[i+1][j]!='●':
                        if board[i+1][j+1]!='●':
                            if board[i+1][j-1]!='●':
                                pass
                            else:
                                if board[i+2][j-2]!='●':
                                    pass
                                else:
                                    if board[i+3][j-3]!='●':
                                        pass
                                    else:
                                        if board[i+4][j-4]!='●':
                                            pass
                                        else:
                                            print('游戏获胜')
                        else:
                            if board[i+2][j+2]!='●':
                                pass
                            else:
                                if board[i+3][j+3]!='●':
                                    pass
                                else:
                                    if board[i+4][j+4]!='●':
                                        pass
                                    else:
                                        print('游戏获胜')
                    else:
                        if board[i+2][j]!='●':
                            pass
                        else:
                            if board[i+3][j]!='●':
                                pass
                            else:
                                if board[i+4][j]!='●':
                                    pass
                                else:
                                    print('游戏获胜')
                else:
                    if board[i][j+2]!='●':
                        pass
                    else:
                        if board[i][j+3]!='●':
                            pass
                        else:
                            if board[i][j+4]!='●':
                                pass
                            else:
                                print('游戏获胜')
            else:
                pass            

#开始下棋
intboard()
printboard()
inputstr=input('请输入您下棋的坐标，应以x,y的格式：\n')
while inputstr != None:
    xstr,ystr=inputstr.split(sep=',')
    if board[int(xstr)-1][int(ystr)-1]=='●':
        print('不能下重复的棋子')
    else:
        board[int(xstr)-1][int(ystr)-1]='●'
        printboard()
        victory()
    inputstr=input('请输入您下棋的坐标，应以x,y的格式：\n')