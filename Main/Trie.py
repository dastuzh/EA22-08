import numpy as np

END = -1

class Trie:
    def __init__(self,arr):
        self.arr = arr
        self.col_names = list(arr.dtype.names)
        self.col_num = len(self.col_names)
        self.arr_len = len(arr)
        self.x = 0
        self.y = 0
        self.cur_sec = arr
        self.atEnd = False

    def open(self,val_name):
        self.atEnd = False
        self.y = self.col_names.index(val_name)
        self.x -= 1



    def get_column_names(self):
        return self.col_names


    def next(self):
        if self.x+1<len(self.cur_sec):
            self.x += 1
            return self.cur_sec[self.x][self.y]
        else:
            return END

    def next2(self):
        if self.x == -1:
            self.x += 1
            return self.arr[self.x][self.y]
        if self.y==0:
            if self.x < self.arr_len:
                self.x += 1
                return self.arr[self.x][self.y]
            else:
                return END
        else: #y>=1 and x != 0
            if self.arr[self.x+1][self.y-1]!=self.arr[self.x][self.y-1]:# at a starting point
                if not self.atEnd:
                    self.x +=1
                    return self.arr[self.x][self.y]
                else:
                    return END
            else:
                self.x += 1
                self.atEnd = True
                return self.arr[self.x][self.y]



    def key(self):
        return self.cur_sec[self.x][self.y]

    def seek(self, seek_key):
        while True:
            n = self.next()
            if n == END:
                return n
            if n>=seek_key: # find a number larger or equal seek_key or reach the end
                return n

    def seek2(self, seek_key):
        while True:
            n = self.next2()
            if n == END:
                # self.atEnd()
                return n
            if n>=seek_key: # find a number larger or equal seek_key or reach the end
                return n

    # def atEnd(self):
    #     print("reach an end")
    #     return False;



    def positioning_by_sequence(self,context,Variable_Order):
        # context is a list of values of variables, etc: [a1,b2,c3]
        # Variable_Order is a list of variables sequence, etc: [x1,x2,x3]
        # this positioning_by_sequence has 2 purpose:
        # 1.check if the trie is iterable for the next valuable
        # 2. if yes set the x-y index(serves as the pointer)
        c = context.copy()
        for i in range(len(Variable_Order)):
            if Variable_Order[i] not in self.col_names:
                try:
                    del c[i]
                except IndexError:
                    pass
        array = self.arr
        for i in range(len(c)):#if c is empty, self.cur_sec equals arr
            indexes = np.where(array[array.dtype.names[i]] == c[i])
            array = array[indexes]
        self.cur_sec = array

        return array.size != 0

    def up(self,context,Variable_Order,val_name):
        c = context.copy()
        for i in range(len(Variable_Order)):
            if Variable_Order[i] not in self.col_names:
                try:
                    del c[i]
                except IndexError:
                    pass
        array = self.arr
        for i in range(len(c)):#if c is empty, self.cur_sec equals arr
            indexes = np.where(array[self.arr.dtype.names[i]] == c[i])
            array = array[indexes]
        print(self.arr.dtype.names)
        try:
            self.x= indexes[0][0]
        except:
            pass
        print(self.x)
        if self.y>0:
            self.y -=1
        # self.y=self.col_names.index(val_name)





