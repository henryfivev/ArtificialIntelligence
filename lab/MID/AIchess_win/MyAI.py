import copy
from ChessBoard import *


class Evaluate(object):
    # 棋子棋力得分
    single_chess_point = {
        'c': 989,   # 车
        'm': 439,   # 马
        'p': 442,   # 炮
        's': 226,   # 士
        'x': 210,   # 象
        'z': 55,    # 卒
        'j': 65536  # 将
    }

    """
    # 马>炮,失败
    single_chess_point = {
        'c': 900,   # 车
        'm': 450,   # 马
        'p': 400,   # 炮
        's': 210,   # 士
        'x': 200,   # 象
        'z': 100,    # 卒
        'j': 60000  # 将
    }
    """
    # 红兵位置得分
    red_bin_pos_point = [
        [9,  9,  9, 11, 13, 11,  9,  9,  9],
        [19, 24, 34, 42, 44, 42, 34, 24, 19],
        [19, 24, 32, 37, 37, 37, 32, 24, 19],
        [19, 23, 27, 29, 30, 29, 27, 23, 19],
        [14, 18, 20, 27, 29, 27, 20, 18, 14],
        [7,  0, 13,  0, 16,  0, 13,  0,  7],
        [7,  0,  7,  0, 15,  0,  7,  0,  7],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0]
    ]
    # 红车位置得分
    red_che_pos_point = [
        [206,208,207,213,214,213,207,208,206],  
        [206,212,209,216,233,216,209,212,206],  
        [206,208,207,214,216,214,207,208,206],  
        [206,213,213,216,216,216,213,213,206],  
        [208,211,211,214,215,214,211,211,208],  
        [208,212,212,214,215,214,212,212,208],  
        [204,209,204,212,214,212,204,209,204],  
        [198,208,204,212,212,212,204,208,198],  
        [200,208,206,212,200,212,206,208,200],  
        [194,206,204,212,200,212,204,206,194] 
    ]
    # 红马位置得分
    red_ma_pos_point = [
        [90, 90, 90, 96, 90, 96, 90, 90, 90],
        [90, 96,103, 97, 94, 97,103, 96, 90],
        [92, 98, 99,103, 99,103, 99, 98, 92],
        [93,108,100,107,100,107,100,108, 93],
        [90,100, 99,103,104,103, 99,100, 90],
        [90, 98,101,102,103,102,101, 98, 90],
        [92, 94, 98, 95, 98, 95, 98, 94, 92],
        [93, 92, 94, 95, 92, 95, 94, 92, 93],
        [85, 90, 92, 93, 78, 93, 92, 90, 85],
        [88, 50, 90, 88, 90, 88, 90, 50, 88]
    ]
    # 红炮位置得分
    red_pao_pos_point = [
        [100,100, 96, 91, 90, 91, 96,100,100],
        [98, 98, 96, 92, 89, 92, 96, 98, 98],
        [97, 97, 96, 91, 92, 91, 96, 97, 97],
        [96, 99, 99, 98,100, 98, 99, 99, 96],
        [96, 96, 96, 96,100, 96, 96, 96, 96],
        [95, 96, 99, 96,100, 96, 99, 96, 95],
        [96, 96, 96, 96, 96, 96, 96, 96, 96],
        [97, 96,100, 99,101, 99,100, 96, 97],
        [96, 97, 98, 98, 98, 98, 98, 97, 96],
        [96, 96, 97, 99, 99, 99, 97, 96, 96],
    ]
    # 红将位置得分
    red_jiang_pos_point = [
        [0,  0,  0,  12000,  12000,  12000,  0,  0,  0],  
        [0,  0,  0,  12000,  12000,  12000,  0,  0,  0],  
        [0,  0,  0,  12000,  12000,  12000,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  9900,  9900,  9900,  0,  0,  0],
        [0,  0,  0,  9930,  9950,  9930,  0,  0,  0],
        [0,  0,  0, 9950, 10000, 9950,  0,  0,  0]
    ]
    # 红相或士位置得分
    red_xiang_shi_pos_point = [
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0, 20,  0,  0,  0, 20,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [18,  0,  0, 20, 23, 20,  0,  0, 18],  
        [0,  0,  0,  0, 23,  0,  0,  0,  0],  
        [0,  0, 20, 20,  0, 20, 20,  0,  0] 
    ]

    red_pos_point = {
        'z': red_bin_pos_point,
        'm': red_ma_pos_point,
        'c': red_che_pos_point,
        'j': red_jiang_pos_point,
        'p': red_pao_pos_point,
        'x': red_xiang_shi_pos_point,
        's': red_xiang_shi_pos_point
    }

    # 黑兵位置得分
    black_bin_pos_point = [
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [7,  0,  7,  0, 15,  0,  7,  0,  7],
        [7,  0, 13,  0, 16,  0, 13,  0,  7],
        [14, 18, 20, 27, 29, 27, 20, 18, 14],
        [19, 23, 27, 29, 30, 29, 27, 23, 19],
        [19, 24, 32, 37, 37, 37, 32, 24, 19],
        [19, 24, 34, 42, 44, 42, 34, 24, 19],
        [9,  9,  9, 11, 13, 11,  9,  9,  9],
    ]
    # 黑车位置得分
    black_che_pos_point = [
        [194,206,204,212,200,212,204,206,194],
        [200,208,206,212,200,212,206,208,200],
        [198,208,204,212,212,212,204,208,198],
        [204,209,204,212,214,212,204,209,204], 
        [208,212,212,214,215,214,212,212,208],  
        [208,211,211,214,215,214,211,211,208],
        [206,213,213,216,216,216,213,213,206], 
        [206,208,207,214,216,214,207,208,206],
        [206,212,209,216,233,216,209,212,206],
        [206,208,207,213,214,213,207,208,206],
    ]
    # 黑马位置得分
    black_ma_pos_point = [
        [88, 50, 90, 88, 90, 88, 90, 50, 88],
        [85, 90, 92, 93, 78, 93, 92, 90, 85],
        [93, 92, 94, 95, 92, 95, 94, 92, 93],
        [92, 94, 98, 95, 98, 95, 98, 94, 92],
        [90, 98,101,102,103,102,101, 98, 90],
        [90,100, 99,103,104,103, 99,100, 90],
        [93,108,100,107,100,107,100,108, 93],
        [92, 98, 99,103, 99,103, 99, 98, 92],
        [90, 96,103, 97, 94, 97,103, 96, 90],
        [90, 90, 90, 96, 90, 96, 90, 90, 90],
    ]
    # 黑炮位置得分
    black_pao_pos_point = [
        [96, 96, 97, 99, 99, 99, 97, 96, 96],
        [96, 97, 98, 98, 98, 98, 98, 97, 96],
        [97, 96,100, 99,101, 99,100, 96, 97],
        [96, 96, 96, 96, 96, 96, 96, 96, 96],
        [95, 96, 99, 96,100, 96, 99, 96, 95],
        [96, 96, 96, 96,100, 96, 96, 96, 96],
        [96, 99, 99, 98,100, 98, 99, 99, 96],
        [97, 97, 96, 91, 92, 91, 96, 97, 97],
        [98, 98, 96, 92, 89, 92, 96, 98, 98],
        [100,100, 96, 91, 90, 91, 96,100,100],
    ]
    # 黑将位置得分
    black_jiang_pos_point = [
        [0,  0,  0, 9950, 10000, 9950,  0,  0,  0],
        [0,  0,  0,  9930,  9950,  9930,  0,  0,  0],
        [0,  0,  0,  9900,  9900,  9900,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  12000,  12000,  12000,  0,  0,  0],  
        [0,  0,  0,  12000,  12000,  12000,  0,  0,  0],  
        [0,  0,  0,  12000,  12000,  12000,  0,  0,  0],  
    ]
    # 黑相或士位置得分
    black_xiang_shi_pos_point = [
        [0,  0, 20, 20,  0, 20, 20,  0,  0],
        [0,  0,  0,  0, 23,  0,  0,  0,  0],
        [18,  0,  0, 20, 23, 20,  0,  0, 18],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0, 20,  0,  0,  0, 20,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
        [0,  0,  0,  0,  0,  0,  0,  0,  0],  
    ]

    black_pos_point = {
        'z': black_bin_pos_point,
        'm': black_ma_pos_point,
        'c': black_che_pos_point,
        'j': black_jiang_pos_point,
        'p': black_pao_pos_point,
        'x': black_xiang_shi_pos_point,
        's': black_xiang_shi_pos_point
    }

    def __init__(self, team):
        self.team = team

    def get_single_chess_point(self, chess: Chess):
        if chess.team == self.team:
            return self.single_chess_point[chess.name]
        else:
            return -1 * self.single_chess_point[chess.name]

    def get_chess_pos_point_r(self, chess: Chess):
        red_pos_point_table = self.red_pos_point[chess.name]
        if chess.team == 'r':
            pos_point = red_pos_point_table[chess.row][chess.col]
        else:
            pos_point = red_pos_point_table[9 - chess.row][chess.col]
        if chess.team != self.team:
            pos_point *= -1
        return pos_point

    def get_chess_pos_point_b(self, chess: Chess):
        black_pos_point_table = self.black_pos_point[chess.name]
        if chess.team == 'b':
            pos_point = black_pos_point_table[chess.row][chess.col]
        else:
            pos_point = black_pos_point_table[9 - chess.row][chess.col]
        if chess.team != self.team:
            pos_point *= -1
        return pos_point

    def evaluate(self, chessboard: ChessBoard):
        point = 0
        if self.team == 'r':
            for chess in chessboard.get_chess():
                point += self.get_single_chess_point(chess)
                point += self.get_chess_pos_point_r(chess)
        else:
            for chess in chessboard.get_chess():
                point += self.get_single_chess_point(chess)
                point += self.get_chess_pos_point_b(chess)
        return point

    # evaluate是对局面的评估,
    # 对于能否吃子的评估需在alphabeta中改进

class ChessMap(object):
    def __init__(self, chessboard: ChessBoard):
        self.chess_map = copy.deepcopy(chessboard.chessboard_map)


"""
现有机制:
1.发现重复走子时,通过加大深度来走出困境
6.当评估值过低时,加大搜索深度

TODO
5.开局中盘不同评估值
---要么开局以动用的棋子为评估值
---要么单纯的使用两套评估值
7.尝试不同的评估函数
---判断阵型,如二鬼拍门之类的
8.引入开局库
9.动态子力

放弃的机制:
2.中盘开启吃子评估
---深度为5时下不过chessai,深度为6时耗时过长
3.时间判断,避免加大深度后运行过长时间
---需要修改alphabeta函数,且意义不大,中途退出可能导致不利局面
4.走出困境后降低深度
---要么使用更多的内存来记录历史棋子以判断是否走出困境,例如：
------使用history_pos来记录所有的new_pos,判断邻近的几步中是否有相同的走法
---要么动态调整搜索深度来实现,但这样操作变多,浪费时间,例如:
------在getnextstep的开始和结束分别depth+=trouble和depth-=trouble,在困境中调整trouble的值

考虑:
1.位置重要还是子力重要
---评估值的影响
---当前子力参考了网上的象棋子力表(乘了100)
2.马重要还是炮重要
---炮重要,当马的评估值大于炮时易失败
3.残局子力是否改变
"""
class MyAI(object):
    def __init__(self, computer_team):
        self.cnt = 0
        self.sum = 0
        self.old_pos = []
        self.new_pos = []
        self.history_pos1 = []
        self.history_pos2 = []
        self.team = computer_team
        if self.team == 'r':
            self.max_depth = 6
        else:
            self.max_depth = 5
        self.evaluate_class = Evaluate(self.team)

    def get_next_step(self, chessboard: ChessBoard):
        self.cnt += 1
        print("现在是第{}回合{}方走子".format(self.cnt, self.team))
        self.old_pos = []
        self.new_pos = []
        val = self.alpha_beta(1, -100000, 100000, chessboard)
        print("eva =", val)
        self.sum += val
        print("sum =", self.sum)
        cur_row,  cur_col  = self.old_pos
        next_row, next_col = self.new_pos
        self.judge_repeat()
        # self.enough_evaluate(self.sum)
        # self.low_evaluate(self.sum)
        self.store_history()
        return cur_row, cur_col, next_row, next_col

    def store_history(self):
        """
        保存上一步和当前的走法
        """
        if self.cnt == 1:
            self.history_pos1 = self.new_pos
        else:
            self.history_pos2 = self.history_pos1
            self.history_pos1 = self.new_pos

    def judge_repeat(self):
        """
        当cnt大于3时,history_pos1和history_pos2
        分别保存着上一步和上上步的走法
        """
        if self.history_pos2 == self.new_pos:
            self.max_depth += 1
            print("发现重复的情况")
            print("已将深度加大至", self.max_depth)
            print("下一回合请耐心等待")
        return 

    def capture_evaluate(self, new_row, new_col, chessboard:ChessBoard):
        if chessboard.chessboard_map[new_row][new_col] != None:
            # 有吃子的情况
            return -0.01 * self.evaluate_class.\
                get_single_chess_point(chessboard.chessboard_map[new_row][new_col])
        else:
            # 无吃子的情况
            return 0

    def enough_evaluate(self, sum):
        if sum > 1000:
            self.max_depth -= 0.2
            print("局面向好")
            print("已将深度减小至", self.max_depth)

    def low_evaluate(self, sum):
        if sum < -100:
            self.max_depth += 0.1
            print("局面不利")
            print("已将深度加大至", self.max_depth)
            print("下一回合请耐心等待")

    def alpha_beta(self, depth, a, b, chessboard:ChessBoard):
        if (depth >= self.max_depth):
            return self.evaluate_class.evaluate(chessboard)
        all_chess = chessboard.get_chess()
        # 遍历棋盘
        for chess in all_chess:
            if (depth%2 == 1 and chess.team == self.team) or \
                (depth%2 == 0 and chess.team != self.team):
                possible_pos = chessboard.get_put_down_position(chess)
                # 遍历该棋子可能的走法
                for next_row, next_col in possible_pos:
                    old_row, old_col = chess.row, chess.col
                    chess_in_new_pos = chessboard.chessboard_map[next_row][next_col]
                    # 移动棋子
                    chessboard.chessboard_map[next_row][next_col] = \
                        chessboard.chessboard_map[old_row][old_col]

                    chessboard.chessboard_map[next_row][next_col].\
                        update_position(next_row, next_col)

                    chessboard.chessboard_map[old_row][old_col] = None
                    # 进入下一层
                    ret = self.alpha_beta(depth+1, a, b, chessboard)
                    # 中盘再加入能否吃子的评估
                    # if self.cnt >= 10:
                    #     ret += self.capture_evaluate(next_row, next_col, chessboard)
                    # 摆回棋子
                    chessboard.chessboard_map[old_row][old_col] = \
                        chessboard.chessboard_map[next_row][next_col]
                    chessboard.chessboard_map[old_row][old_col].\
                        update_position(old_row, old_col)
                    chessboard.chessboard_map[next_row][next_col] = chess_in_new_pos
                    # 保存与剪枝
                    if (depth%2 == 1):
                        if (ret > a or self.old_pos == []) and depth == 1:
                            # 保存get_next_step的返回值
                            self.old_pos = [chess.row, chess.col]
                            self.new_pos = [next_row, next_col]
                        a = max(a, ret)
                    else:
                        b = min(b, ret)
                    if (a >= b):
                        if (depth%2 == 1):
                            return a
                        else:
                            return b
        if (depth%2 == 1):
            return a
        else:
            return b
