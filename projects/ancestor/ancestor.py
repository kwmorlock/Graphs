
# Write a function that, given the dataset and the ID
#  of an individual in the dataset, returns their earliest known ancestor
#   – the one at the farthest distance from the input individual. 
#   If there is more than one ancestor tied for "earliest", return the 
#   one with the lowest numeric ID. If the input individual has no parents, 
#   the function should return -1.

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    # pass

    q = Queue() # Create an empty queue