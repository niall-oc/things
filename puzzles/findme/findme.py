# -*- coding: utf-8 -*-
from random import random, seed
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def validate_entity(entity, config):
    """
    If no bounds or entities are properly defined.
    OR
    If the entities are out of bounds.
    """
    if any([entity[0] < config['top_left'][0], entity[1] < config['top_left'][1],
            entity[0] > config['bottom_right'][0], entity[1] > config['bottom_right'][0]]):
        return False
    return True


def get_move(entity, config):
    """
    Given a grid X by Y blocks insize a new move must respect the following.

    A move is either along the x axis or the y axis but not both.
    A move is only one block.
    A move cannot be outside the lower bound x,y or the upper bound x,y.
    """
    move_x = bool(random() > .5)
    move = 1 if bool(random() > .5) else -1
    if move_x:
        new_entity = [entity[0] + move, entity[1]]
        if not validate_entity(new_entity, config):
            new_entity = [entity[0] - move, entity[1]]
    else:
        new_entity = [entity[0], entity[1] + move]
        if not validate_entity(new_entity, config):
            new_entity = [entity[0], entity[1] - move]
    return new_entity


def start_game(config):
    """
    Will keep going until the man finds the flag
    """
    seed()
    if validate_entity(config['man'], config) and validate_entity(config['flag'], config):

        move_trace = [config['man']]
        new_man = get_move(config['man'], config)
        while new_man != config['flag']:
            logger.info("%s %s", new_man, config['flag'])
            move_trace.append(new_man)
            new_man = get_move(new_man, config)
        return move_trace

    else:
        print('Man and flag must be in bounds')


if __name__ == '__main__':
    import sys
    import json

    logger.info("BEGINING")
    with open("/home/niall/Software/things/puzzles/findme/config.json", "r") as f:
        config = json.loads(f.read())

    logger.info("CONFIG : %s", config['flag'])

    results = [len(start_game(config)) for i in range(config['paths'])]
    print()
    print('Max', max(results))
    print('Min', min(results))
    avg = sum(results)/config['paths']
    print('Avg : %s' % avg)
    dev = [abs(avg-i) for i in results]
    # print('Dev : %s' % dev)
    stv = sum(dev)/config['paths']
    print('Stv : %s' % stv)
