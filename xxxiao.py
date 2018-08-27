import copy

class Board(list):
    ROW = 13
    def __init__(self, *rows):
        if len(rows) > Board.ROW:
            raise Exception('RowOutOfBoard')
        super().__init__(rows)
    
    def play(self, motion, pre_row):
        self.move(motion)
        self.drop()
        self.insert(0, pre_row)
        self.drop()
    
    def copy(self):
        return copy.deepcopy(self)

    def move(self, motion):
        row, index, step = motion
        return self[row].move(index, step)

    def __drop(self, above, below):
        count = 0
        for i in range(len(above)):
            if below.append(above[i]):
                above[i] = None
                count += 1
        try:
            while True:
                del above[above.index(None)]
        except ValueError:
            pass
        return count
    
    def drop(self):
        flag = False
        count = 0
        while True:
            n = len(self) - 1
            if n < 1:
                return count
            for i in range(n):
                if self.__drop(self[i+1], self[i]) > 0:
                    flag = True
            if flag:
                flag = False
            else:
                crow = self.disappear()
                if crow == 0:
                    return count
                count += crow

    def disappear(self):
        # 经典错误写法
        # for r in range(len(self)):
        #     if self[r].full():
        #         del self[r]
        count = 0
        for r in range(len(self)):
            if self[r].full():
                self[r].clear()
                count += 1
        try:
            while True:
                del self[self.index([])]
        except ValueError:
            pass
        return count
    
    def __str__(self):
        return ''.join([str(row) + '\n' for row in self[::-1]])


class Row(list):
    CLOUMN = 9
    def __init__(self, *bars):
        for bar in bars:
            if not self.append(bar):
                raise Exception('BadInitialize')
    
    def full(self):
        sum = 0
        for bar in self:
            sum ^= bar.bin()
        return sum == (1 << Row.CLOUMN) - 1
    
    def copy(self):
        return copy.deepcopy(self)


    def append(self, bar):
        return self.insert(len(self), bar)

    
    def insert(self, index, bar):
        for inner_bar in self:
            if bar.bin() & inner_bar.bin() != 0:
                return False
        super().insert(index, bar)
        return True
    
    def move(self, index, step):
        if step == 0:
            return True
        bar_copy = self[index].copy()
        if not bar_copy.move(step):
            return False
        bar = self.pop(index)
        if not self.insert(index, bar_copy):
            super().insert(index, bar)
            return False
        return True
    
    def index(self, col):
        if type(col) != int:
            return super().index(col)
        
        for i in range(len(self)):
            if self[i].distance == col:
                return i
        raise Exception('NoBar')

    def __str__(self):
        rs = ['  ' for n in range(Row.CLOUMN)]
        for i in range(len(self)):
            bar = self[i]
            for j in range(bar.width):
                rs[bar.distance + j] = Bar.GRAPH[i]
        return ' '.join(rs)


class Bar():
    GRAPH = ('▤', '▥', '▧', '▨', '▦', '▩', '◒', '◓')
    def __init__(self, distance, width):
        if width <= 0 or not Bar.__check(distance, width):
            raise Exception('NonBar')
        
        self.distance = distance
        self.width = width
        
    #@param step 左减 右加
    def move(self, step):
        if step == 0:
            return True
        if not Bar.__check(self.distance + step, self.width):
            return False
        self.distance += step
        return True

    def copy(self):
        return copy.copy(self)

    def bin(self):
        return ((1 << self.width) - 1) << self.distance
    
    @staticmethod
    def __check(distance, width):
        return distance >= 0 and distance + width <= Row.CLOUMN

    def __str__(self):
        return bin(self.bin()[:1:-1])