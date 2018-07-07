import bottle
import os
import random
import math
from Helpers import *
from astar import *


TAUNTS = [
    "You wanna piece of me? C'mon!",
    "Chicken! Fight Like a Snake!",
    "Iff yoo hert maaee baybeez Aaeell rost yoo ahlive",
    "I'll be back!",
    "You fight like a dairy farmer!",
    "Impossible Mission!",
    "I never asked your sister out!",
    "Stick to the pond, froggy!",
    "Butt-kicking for goodness!",
    "Hey! You! Snaky!",
    "Run Forrest, run!",
    "Who's slow now?!",
    "PushThePowerButton",
    "Marry Me?? <3",
    "Hands off my tail",
    "yololo",
    "I just wanna tell you how I'm feeling",
    "Gotta make you understand",
    "We've known each other for so long",
    "Wat up? :p",
    "BOODERS"
]

COLORS = [
    "#008080",
    "#EAA118",
    "#3F18EA",
    "#EE0BCD",
    "#4CEE0B"
]

#global variables
BOARD_HIGHT=0
BOARD_WIDTH=0
SNAKE_COUNT=0
BOARD_DATA = []
GAME_ID = ''
OUR_SNAKE_ID = ''

#global snake's data



@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    global GAME_ID
    GAME_ID = data['game_id']
    global BOARD_WIDTH
    BOARD_WIDTH = data['width']
    global BOARD_HIGHT
    BOARD_HIGHT = data['height']

    global OUR_SNAKE_ID
    OUR_SNAKE_ID = data['you']

    head_url = '%s://%s/static/snake.gif' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': random.choice(COLORS),
        'taunt': '{} ({}x{})'.format(GAME_ID, BOARD_WIDTH, BOARD_HIGHT),
        'head_url': head_url,
        'name': '!HypnoSnake$'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

#variables
    food = data['food']
    ALL_SNAKES = data['snakes']
    DEAD_SNAKES = data['dead_snake']
    snakes = all_snake_locations(data.get("snakes"))
    ourSnakeHead = get_our_snake_position(data.get("snakes"), OUR_SNAKE_ID)
    borders = get_borders_coords(data["height"], data["width"])




    moveDirection = None

    directions = ["west", "north", "south", "east"]
    options = []
    #west
    options.append(is_empty([ourSnakeHead[0]-1, ourSnakeHead[1]], food, snakes, borders))
    #north
    options.append(is_empty([ourSnakeHead[0], ourSnakeHead[1]-1], food, snakes, borders))
    #south
    options.append(is_empty([ourSnakeHead[0], ourSnakeHead[1]+1], food, snakes, borders))
    #east
    options.append(is_empty([ourSnakeHead[0]+1, ourSnakeHead[1]], food, snakes, borders))

    #if there is food
    if "food" in options:
        moveDirection = directions[options.index("food")]
    else:

        if food!=[]:
            moveDirection = 'west'
            closest_food = closest_food_coord(ourSnakeHead, food)

            horizontal = ''
            if closest_food[0] > ourSnakeHead[0]:
                #to east
                horizontal = 'east'
            elif closest_food[0] < ourSnakeHead[0]:
                # to west
                horizontal = 'west'
            elif closest_food[0] == ourSnakeHead[0]:
                #same horizontal
                horizontal = 'none'

            vertical = ''
            if closest_food[1] > ourSnakeHead[1]:
                #to south
                vertical = 'south'
            elif closest_food[1] < ourSnakeHead[1]:
                # to north
                vertical = 'north'
            elif closest_food[1] == ourSnakeHead[1]:
                #same horizontal
                vertical = 'none'

            moveDirection = None
            if horizontal == 'west' and options[0] == 'empty' and ourSnakeHead[0] != 0:
                moveDirection = 'west'
            elif horizontal == 'east' and options[3] == 'empty' and ourSnakeHead[0]!= board_width-1:
                moveDirection = 'east'
            elif vertical == 'north' and options[1] == 'empty' and ourSnakeHead[1] != 0:
                moveDirection = 'north'
            elif vertical == 'south' and options[2] == 'empty' and ourSnakeHead[1] != board_height-1:
                moveDirection = 'south'

    if moveDirection == None:
        for i in range(0,4):
            if options[i] == "empty":
                moveDirection = directions[i]





# TODO: Do things with data
    #directions = ['up', 'down', 'left', 'right']




    return {
        'move': moveDirection,
        'taunt': random.choice(TAUNTS)
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
