from xxxiao import Bar, Row, Board

def solve(pre_row):
    results = {}
    for motion in motions(board):
        board_copy = board.copy()
        board_copy.move(motion)
        count = board_copy.drop()
        
        pre_row_copy = pre_row.copy()
        board_copy.insert(0, pre_row_copy)
        count += board_copy.drop()
        if count > 0:
            results[motion] = (count, 0)
        for motion2 in motions(board_copy):
            board_copy2 = board_copy.copy()
            board_copy2.move(motion2)
            count2 = board_copy2.drop()
            if count2 > 0:
                results[motion] = (count, count2)
    return sorted(results.items(), \
        key=lambda t: t[1], reverse=True)

def motions(board):
    m = []
    board_copy = board.copy()
    step = -1
    for r in range(len(board)):
        for i in range(len(board[r])):
            while True:
                if board_copy.move((r, i, step,)):
                    m.append((r, i, step))
                    step += -1 if step <= 0 else 1
                    board_copy = board.copy()
                else:
                    if step > 0:
                        step = -1
                        break
                    step = 1
    return m

def parse_row(cbars):
    from functools import reduce
    row_t = [int(s) for s in cbars]
    row = Row()
    for i in range(len(cbars)):
        if row_t[i] > 0:
            row.append(Bar(reduce(\
                lambda a, b: abs(a) + abs(b), row_t[:i], 0),\
                row_t[i]))
    return row

import re
spaces = re.compile(r'\s+')

board = Board()
while True:
    try:
        cbars = spaces.split(input('init> ').strip())
        board.insert(0, parse_row(cbars))
    except (KeyboardInterrupt, EOFError):
        print()
        print(board)
        break
    except Exception as e:
        print(e)

while True:
    try:
        args = spaces.split(input('xxxiao> ').strip())

        jump = False
        if args[0] == 'x':
            board[int(args[1]) - 1] = parse_row(args[2:])
            jump = True
        elif args[0] == 'i':
            board.insert(int(args[1]) - 1, parse_row(args[2:]))
            jump = True
        elif args[0] == 'd':
            del board[int(args[1]) - 1]
            jump = True
        
        if jump:
            print(board)
            continue

        pre_row = parse_row(args)
        results = solve(pre_row)

        for ii in range(len(results)):
            r, i, s = results[ii][0]
            c1, c2 = results[ii][1]
            print('%2d: 第%2d行，第%2d列，移%2d下，可消%d层，再移可消%d层，共消%d层' % \
                (ii + 1, r+1, board[r][i].distance + 1, s, c1, c2, c1+c2))
        while True:
            try:
                motion = spaces.split(input('move> ').strip())
                m = None
                if len(motion) == 1:
                    m = results[int(motion[0]) - 1][0]
                else:
                    row = int(motion[0]) - 1
                    index = board[row].index(int(motion[1]) - 1)
                    step = int(motion[2])
                    m = (row, index, step)
                board.play(m, pre_row)
                break
            except (KeyboardInterrupt, EOFError):
                break
            except Exception as e:
                print(e)
        print(board)
    except (KeyboardInterrupt, EOFError):
        break
    except Exception as e:
        print(e)