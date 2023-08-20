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
        self.stack = list()
        self.queue = list()
        

    def push(self, x):
        self.stack.insert(0, x)

    def pop(self):
        if len(self.queue) == 0:
            self._move()
        return self.queue.pop(0)
        

    def peek(self):
        if len(self.queue) == 0:
            self._move()
        return self.queue[0]

    def _move(self):
        while len(self.stack) > 0:
            self.queue.insert(0, self.stack.pop(0))


    def empty(self):
        return len(self.queue) + len(self.stack) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()