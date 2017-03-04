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


#GET OUR SNAKE INFO

#return array of our snake coords
def get_our_snake_position(snakes, OUR_SNAKE_ID):
    for i in range(0, len(snakes)):
        if snakes[i].get("id") == OUR_SNAKE_ID:
            return snakes[i].get("coords")[0]


#array points of all enemies
def all_snake_locations(snakes):
    snake_locations = []

    for snake in snakes:
        this_snake = snake.get("coords")
        for coords in this_snake:
            snake_locations.append(coords)

    return snake_locations


def get_borders_coords(b_height, b_width):
    borders = []
    for i in range(b_height):
        #add horizontal borders
        borders.append([-1, i])
        borders.append([b_height, i])

    for j in range(b_width):
        #add vertical borders
        borders.append([j, -1])
        borders.append([j, b_width])
    return borders


#take [x,y] as coordinates
def what_is_cell(coordinates, food, snakes, borders):
    if coordinates in food:
        return "food"
    #check boarders??
    elif coordinates in snakes:
        return "snake"
    elif coordinates in borders:
        return "wall"
    else:
        return "empty"


