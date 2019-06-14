# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.


class Stack:

    def __init__(self, num=None):
        self.__data = [] if num is None else [num]
        self.__min = [] if num is None else [0]

    def is_empty(self):
        return len(self.__data) == 0

    def push(self, num):
        if not self.is_empty():
            if self.__data[self.__min[-1]] > num:
                self.__min.append(len(self.__data))
        else:
            self.__min.append(0)
        self.__data.append(num)

    def pop(self):
        if not self.is_empty():
            if len(self.__data) - 1 == self.__min[-1]:
                self.__min.pop()
            return self.__data.pop()

    @property
    def min(self):
        return self.__data[self.__min[-1]] if not self.is_empty() else None
