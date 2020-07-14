"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy

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


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # 

        self.vertices[vertex_id] = set() #this will hold edges



    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass  #
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) #there is an edge from v1 to v2
        else:
            raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  #
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass  #

        q = Queue() # Create an empty queue

        q.enqueue(starting_vertex) # Init: enqueue the starting node

        visited = set() # Create a set to store the visited nodes


        while q.size() > 0: # While the queue isn't empty

            v = q.dequeue() # Dequeue the first item

            if v not in visited: # If it's not been visited:
                print(v)
                visited.add(v)  # Mark as visited (i.e. add to the visited set)

                # print(f"Visited {v}") # Do something with the node

                neighbors = self.get_neighbors(v) #getting neighbors

                for neighbor in neighbors: #checking for each neighbor

                    q.enqueue(neighbor) #adding it to the que

                # for next_vert in self.get_neighbors(v): # Add all neighbors to the queue
                #     q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  #
        s = Stack() # Create an empty stack

        s.push(starting_vertex) # Init: push the starting node

        visited = set()# Create a set to store the visited nodes


        while s.size() > 0: # While the stack isn't empty

            v = s.pop()  # pop the first item

            if v not in visited: # If it's not been visited:
                print(v)
                visited.add(v) # Mark as visited (i.e. add to the visited set)

                # print(f"Visited {v}") # Do something with the node
                neighbors = self.get_neighbors(v)
                for neighbor in neighbors:
                    s.push(neighbor) #not real python method from python library, check uptop

                # for next_vert in self.get_neighbors(v):  # Add all neighbors to the stack
                #     s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()): #calling the function, having visited set to an empty set, we want our function to do what the previous dft can do
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass  #

        if starting_vertex not in visited: #we had to define visited in recursive function for it to be defined

            visited.add(starting_vertex) #if not in visited we add in visited set

            print(starting_vertex)

            for neighbor in self.vertices[starting_vertex]: #loop through each neighbor for each vertex and then call the function
                self.dft_recursive(neighbor, visited) #will call it recursively
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  #

        q = Queue() # Create an empty queue and enqueue A PATH TO the starting vertex ID

        visited = set() # Create a Set to store visited vertices

        q.enqueue([starting_vertex])

        while q.size() > 0: # While the queue is not empty...

            v = q.dequeue()  # Dequeue the first PATH

            node = v[-1] # Grab the last vertex from the PATH

            if node not in visited: # If that vertex has not been visited...
                if node == destination_vertex:  # CHECK IF IT'S THE TARGET
                    return v  # IF SO, RETURN PATH

                visited.add(node) # Mark it as visited...

                for friend in self.vertices[node]: # Then add A PATH TO its neighbors to the back of the queue
                    new = v.copy() # COPY THE PATH

                    new.append(friend) # APPEND THE NEIGHOR TO THE BACK

                    q.enqueue(new)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  #

        s = Stack() #create empty stack

        s.push([starting_vertex]) #initialize path to starting vertex

        visited = set() #create empty set that will keep track of visited

        while s.size() > 0: #while stack is not empty

            path = s.pop() #remove our first path

            node = path[-1] #then grab our last item on path

            if node not in visited: #if not in visited
                if node == destination_vertex: #if node matches target
                    return path

                visited.add(node) #mark that as visited

                for neighbor in self.vertices[node]: #check for all neighbor
                    new_path = path.copy() #add a new path to its neighbors, by copying it

                    new_path.append(neighbor) #add the neighbor into the new path
                    s.push(new_path) #push new path into the stack

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]): #initializing with empty visiting set and empty path
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  #

        visited.add(starting_vertex) #add a starting vertex into visited
        path = path + [starting_vertex] #add path to starting vertex

        if starting_vertex ==  destination_vertex: #return the path
            return path

        for neighbor in self.get_neighbors(starting_vertex): #loop through all the vertex neighbors
            if neighbor not in visited: #if neighbor hasnt been visited we will create a path by calling function recursively

                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)

                if new_path is not None: #if the path isnt none then just return the path
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
