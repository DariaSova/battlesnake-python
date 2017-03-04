


#pass food array and head coordinate as [x,y]
def closest_food_coord(head, food):
    food_distances=[]
    steps_num = []

    #make a list with distances head<->food item
    for f in food:
        food_distances.append(distance(head[0], head[1], f[0], f[1]))
        this_food_distances = distance(head[0], head[1], f[0], f[1])
        #how many steps needed to get that food item
        steps_num.append(this_food_distances)

    ind = steps_num.index(min(steps_num))
    return food[ind]

def distance(x1, y1, x2, y2):
    distance = []
    x_dist = x1-x2
    y_dist = y1-y2
    # distance.append(x_dist)
    # distance.append(y_dist)
    res = abs(x_dist) + abs(y_dist)
    return res
