#!usr/bin/env python

from Queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0

        # If parent is plugged in (little unsure ?)
        if parent:
            self.path = parent.path[:] #make copy of list into own list
            self.path.append(value) #put own value into path
            self.start = parent.start
            self.goal = parent.goal
        # If there is no parent start a path with current state
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def GetDist(self):
        pass
    def CreateChildren(self):
        pass

class State_String(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(State_String, self).__init__( # initialize base class - State class
                value, parent, start, goal)
        self.dist = self.GetDist #set distance

    def GetDist(self):
        # Check to see if we have reached our goal
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)): # Go through each letter of the goal
            letter = self.goal[i] # Get current letter
            # Distance letter is from target placement
            dist += abs(i - self.value.index(letter)) # This part is a bit confusing
        return dist

    def CreateChildren(self):
        if not self.children:
            for i in xrange(len(self.goal)-1):
                # make copy of val
                val = self.value
                # switch second letter and first letter of every pair of letters (? on this)
                val = val[:i] + val[i+1] + val[i] + val[i+2]
                child = State_String(val, self)
                self.children.append(child)

class AStar_Solver:
    def __init__(self, start, goal):
        self.path = [] #store final path
        self.visitedQueue = [] #all chilren we already visited
        self.priorityQueue = PriorityQueue
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_String(self.start,
                                  0, #there is no parent passed in start staete
                                  self.start,
                                  self.goal)
        count = 0
        self.priorityQueue.put((0, count, startState)) #pass tuple, 0 is priority number?, add this tuple to queue
        #while path is empty and queue has a size
        while(not self.path and self.priorityQueue.qsize()):
            #get top most state and get state from tuple
            closestChild = self.priorityQueue.get()[2]
            closestChild.CreateChildren() #create childre
            self.visitedQueue.append(closestChild.value) # add child to visited children
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count += 1
                    # if child's distance is at 0 and does not exist
                    if not child.dist:
                        # found solution, take this path
                        self.path = child.path
                        break
                    self.priorityQueue.put()
        if not self.path:
            print "Goal of " + self.goal + " is not possible"
        return self.path

if __name__ == "__main__":
    start1 = "hma"
    goal1 = "ham"
    print 'starting...'
    a = AStar_Solver(start1, goal1)
    a.Solve()
    for i in xrange(len(a.path)):
        print "%d) " %i + a.path[i]

