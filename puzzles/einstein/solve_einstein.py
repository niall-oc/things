import einstein
from pprint import pprint
from copy import deepcopy

def rule1(state):
    """
    The Brit lives in a red house.
    """
    return einstein.propose_value('house_color', 'red', 'nationality', 'british', state)

def rule2(state):
    """
    The Swede keeps dogs.
    """
    return einstein.propose_value('nationality', 'swedish', 'pet', 'dog', state)

def rule3(state):
    """
    The Dane drinks tea.
    """
    return einstein.propose_value('nationality', 'dane', 'drink', 'tea', state)

def rule4(state):
    """
    The green house is on the left of the white house.
    """
    house = einstein.get_position('green', state)
    if house:
        return einstein.assign_value(einstein.left_of(house), 'house_color', 'white', state)
    else:
        return state

def rule5(state):
    """
    The green house owner drinks coffee.
    """
    house = einstein.get_position('green', state)
    if house:
        return einstein.assign_value(house, 'drink', 'coffee', state)
    else:
        return state

def rule6(state):
    """
    The person who plays polo rears birds.
    """
    return einstein.propose_value('sport', 'polo', 'pet', 'bird', state)

def rule7(state):
    """
    The owner of the yellow house plays hockey.
    """
    return einstein.propose_value('house_color', 'yellow', 'sport', 'hockey', state)

def rule8(state):
    """
    The man living in the house right in the center drinks milk.
    """
    return einstein.assign_value('3', 'drink', 'milk', state)
    
def rule9(state):
    """
    The Norwegian lives in the first house.
    """
    return einstein.assign_value('1', 'nationality', 'norweigen', state)

def rule10(state):
    """
    The man who plays baseball lives next to the man who keeps cats.
    """
    baseball_house = einstein.get_position('baseball', state)
    cat_house = einstein.get_position('cat', state)
    if cat_house and baseball_house: # We have assigned these rules already
        return state
    elif cat_house: # We only know where the cat lives
        return einstein.propose_house(einstein.next_of(cat_house), 'sport', 'baseball', state)
    elif baseball_house:# we only know where the baseball lives
        return einstein.propose_house(einstein.next_of(baseball_house), 'pet', 'cat', state)
    else: # We don't know where either the baseball or cat live
        return state

def rule11(state):
    """
    The man who keeps horses lives next to the one who plays hockey.
    """
    hockey_house = einstein.get_position('hockey', state)
    horse_house = einstein.get_position('horse', state)
    if horse_house and hockey_house: # We have assigned these rules already
        return state
    elif horse_house: # We only know where the horse lives
        return einstein.propose_house(einstein.next_of(horse_house), 'sport', 'hockey', state)
    elif hockey_house:# we only know where the hockey lives
        return einstein.propose_house(einstein.next_of(hockey_house), 'pet', 'horse', state)
    else: # We don't know where either the hockey or horse live
        return state

def rule12(state):
    """
    The man who plays billiards drinks beer.
    """
    return einstein.propose_value('sport', 'billiards', 'drink', 'beer', state)

def rule13(state):
    """
    The German plays soccer.
    """
    return einstein.propose_value('nationality', 'german', 'sport', 'soccer', state)

def rule14(state):
    """
    The Norwegian lives next to the blue house.
    """
    norweigen = einstein.get_position('norweigen', state)
    if not norweigen:
        return state
    else:
        houses = einstein.next_to(norweigen)
        if len(houses) == 1:
            return einstein.assign_value('2', 'house_color', 'blue', state)
        else:
            return einstein.propose_house(houses, 'house_color', 'blue', state)

def rule15(state):
    """
    The man who plays baseball has a neighbor who drinks water.
    """
    baseball_house = einstein.get_position('baseball', state)
    water_house = einstein.get_position('water', state)
    if baseball_house and water_house: # We have assigned these rules already
        return state
    elif water_house: # We only know where the water lives
        return einstein.propose_house(einstein.next_of(water_house), 'sport', 'baseball', state)
    elif baseball_house:# we only know where the baseball lives
        return einstein.propose_house(einstein.next_of(baseball_house), 'drink', 'water', state)
    else: # We don't know where either the baseball or water live
        return state

def solve(state):
    """

    """
    rule_list = [
        rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
        rule9, rule10, rule11, rule12, rule13, rule14, rule15
    ]
    for puzzle_iteration in xrange(100):
        for rule in rule_list:
            state = einstein.elimination_sweep(rule(state))
            if einstein.end_solution(state):
                return state, puzzle_iteration
    return state, puzzle_iteration
        
           

if __name__ == '__main__':
    state = deepcopy(einstein.START_STATE)
    state, puzzle_iteration = solve(state)
    pprint(state)
    print "Stopped at iteration {0}".format(puzzle_iteration)
    einstein.print_solution(state)
