#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import random, seed

TOP_LEFT = None
BOTTOM_RIGHT = None

def validate_entity(entity):
    """
    If no bounds or entities are properly defined.
    OR
    If the entities are out of bounds.
    """
    if any([ entity[0] < TOP_LEFT[0], entity[1] < TOP_LEFT[1],
             entity[0] > BOTTOM_RIGHT[0], entity[1] > BOTTOM_RIGHT[0] ]):
        return False
    return True

def get_move(entity):
    """
    Given a grid X by Y blocks insize a new move must respect the following.
        
    A move is either along the x axis or the y axis but not both.
    A move is only one block.
    A move cannot be outside the lower bound x,y or the upper bound x,y.
    """
    move_x = bool(random() > .5)
    move = 1 if bool(random() > .5) else -1
    if move_x:
        new_entity = (entity[0] + move, entity[1])
        if not validate_entity(new_entity):
            new_entity = (entity[0] - move, entity[1])
    else:
        new_entity = (entity[0], entity[1] + move)
        if not validate_entity(new_entity):
            new_entity = (entity[0], entity[1] - move)
    return new_entity

def start_game(top_left, bottom_right, man, flag):
    """
    Will keep going until the man finds the flag
    """
    global TOP_LEFT, BOTTOM_RIGHT
    seed()
    TOP_LEFT = top_left
    BOTTOM_RIGHT = bottom_right
    if validate_entity(man) and validate_entity(flag):
    
        move_trace = [man]
        while man != flag:
            man = get_move(man)
            move_trace.append(man)
        return move_trace
            
    
    else:
        print 'Man and flag must be in bounds'

if __name__ == '__main__':
    import sys, getopt
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:b:m:f:p:", ["topleft=", "bottomright", "man=", "flag=", "paths="])
    except getopt.GetoptError:
        print '\nUsage: findme.py -t <top left> -b <bottom right> -m <man> -f <flag>\n\neg python findme.py -t0,0 -b3,3 -m1,0 -f3,3'
        sys.exit(2)
    tl = None
    br = None
    man = None
    flag = None
    for opt, arg in opts:
        if opt in ('-t', '--topleft'):
            tl = tuple([int(i) for i in arg.split(',')])
        if opt in ('-b', '--bottomright'):
            br = tuple([int(i) for i in arg.split(',')])
        if opt in ('-m', '--man'):
            man = tuple([int(i) for i in arg.split(',')])
        if opt in ('-f', '--flag'):
            flag = tuple([int(i) for i in arg.split(',')])
        if opt in ('-p', '--paths'):
            paths = int(arg)
            
    
    results = [len(start_game(tl, br, man, flag)) for i in range(paths)]
    print results
    print 'Max', max(results)
    print 'Min', min(results)
    avg = sum(results)/paths
    print 'Avg', avg
    dev = [abs(avg-i) for i in results]
    print 'Dev', dev
    stv = sum(dev)/paths
    print 'Stv', stv
    
