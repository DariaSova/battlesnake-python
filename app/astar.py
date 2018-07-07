from Helpers import *

#ourSnakeHead = [x, y]
def aStar(ourSnakeHead, goal, food, snakes, borders):
    #The open and closed sets
    openset = set()
    closedset = set()
    #Current point is the ourSnakeHeading point
    current = ourSnakeHead
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:

        #Find the item in the open set with the lowest G + H score
        current = openset.pop()
        #If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        #Add it to the closed set
        closedset.add(current)
        #Loop through the node's children/siblings

        #this is four possible steps we could take
        options = []
#west
        if what_is_cell([ourSnakeHead[0]-1, ourSnakeHead[1]], food, snakes, borders):
            options.append([ourSnakeHead[0]-1, ourSnakeHead[1]])
#north
        if what_is_cell([ourSnakeHead[0], ourSnakeHead[1]-1], food, snakes, borders):
            options.append([ourSnakeHead[0], ourSnakeHead[1]-1])
#south
        if what_is_cell([ourSnakeHead[0], ourSnakeHead[1]+1], food, snakes, borders):
            options.append([ourSnakeHead[0], ourSnakeHead[1]+1])
#east
        if what_is_cell([ourSnakeHead[0]+1, ourSnakeHead[1]], food, snakes, borders):
            options.append([ourSnakeHead[0]+1, ourSnakeHead[1]])



        for option in options:
            #If it is already in the closed set, skip it
            if option in closedset:
                continue
            #Otherwise if it is already in the open set
            if option in openset:
                #Check if we beat the G score 
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')