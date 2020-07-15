
# Write a function that, given the dataset and the ID
#  of an individual in the dataset, returns their earliest known ancestor
#   – the one at the farthest distance from the input individual. 
#   If there is more than one ancestor tied for "earliest", return the 
#   one with the lowest numeric ID. If the input individual has no parents, 
#   the function should return -1.

#set starting_node?
#if higher number return lowest value
#if 0 return -1


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

    p = [starting_node] #first node to path

    q.enqueue(p) # Init: enqueue the starting

    while q.size() > 0: # While the queue isn't empty
        curr = q.dequeue() # Dequeue the first item

        newish = []

        change = False  #boolean variable set to false

        for node in curr: #loop through each node in the current path
            for ancestor in ancestors: #checking for each ancestor 
                if ancestor[-1] == node: #if last matches node 
                    newish.append(ancestor[0]) #add the ancestor, added to first spot
                    change = True #change is true because ancestor exists
                    q.enqueue(newish) # Init: enqueue the new path

        if change is False: #if hasnt changed // no ancestor 
            if curr[0] == starting_node: #if current path matches starting node // has no ancestor since first
                return -1 #no parents
            else:
                return curr[0] #is an ancestor and will be returned
