class MyQueue(object):
    # pu 1, pu 2, peek, pop, pop, peek => [N, N, 2, 2, 1, N]
    # peek => [N]
    # pop => [N]
    # pu 1, pop, pop => N, 1, N
    #
    # push E => pop all elements from s1 to s2, add E, pop back
    # peek => return top from the s2
    # pop => return from the s3 and remove (pop)
    # size => size of s2
    def __init__(self):
        self.main = list()
        self.temp = list()
        

    def push(self, x):
        for el in self.main:
            self.temp.insert(0, el)
        del self.main[:]
        self.main.append(x)
        for el in self.temp:
            self.main.insert(0, el)
        del self.temp[:]
        

    def pop(self):
        return self.main.pop(0)
        

    def peek(self):
        return self.main[0]        

    def empty(self):
        return len(self.main) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()