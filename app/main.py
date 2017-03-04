import bottle
import os
import random
import math
from helpers import *


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
    FOOD = data['food']
    ALL_SNAKES = data['snakes']
    DEAD_SNAKES = data['dead_snake']
    all_snakes_coords = snakeLocations(data.get("snakes"))
    ourSnakeHead = get_our_snake_position(data.get("snakes"), OUR_SNAKE_ID)
    borders = get_borders_coords(data["height"], data["width"])




    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': random.choice(directions),
        'taunt': random.choice(TAUNTS)
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
