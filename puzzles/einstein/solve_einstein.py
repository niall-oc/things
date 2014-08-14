import einstein
from pprint import pprint
from copy import deepcopy
import pdb

def rule1(state):
    """The Brit lives in a red house."""
    return einstein.propose_value('house_color', 'red', 'nationality', 'british', state)

def rule2(state):
    """The Swede keeps dogs."""
    return einstein.propose_value('nationality', 'swedish', 'pet', 'dog', state)

def rule3(state):
    """The Dane drinks tea."""
    return einstein.propose_value('nationality', 'danish', 'drink', 'tea', state)

def rule4(state):
    """The green house is on the left of the white house."""
    green_house = einstein.get_position('green', state)
    white_house = einstein.get_position('white', state)
    # Green and white are already defined
    if green_house and white_house:
        return state
    # Green is defined so we can define white
    elif green_house:
        return einstein.assign_value(einstein.right_of(house), 'house_color', 'white', state)
    # White is defined so we can define green
    elif white_house:
        return einstein.assign_value(einstein.right_of(house), 'house_color', 'white', state)
    # Neither Green or White are defined
    else:
        # Go through all houses and make the following assertions
        for house in state.keys():
            house_to_right = einstein.right_of(house)
            house_to_left = einstein.left_of(house)
            # Nothing on the left so this cannot be the white house
            if not house_to_left:
               state = einstein.remove_value(house, 'house_color', 'white', state)
            # nothing o the right so this cannot be the green house
            elif not house_to_right:
                state = einstein.remove_value(house, 'house_color', 'green', state)
            if house_to_right:
                has_green = 'green' in state[house]['house_color']
                white_to_right = 'white' in state[house_to_right]['house_color']
                # If this house has green in its color list
                # AND this house is NOT left of a white house
                # THEN green must be removed from this house
                if has_green and not white_to_right:
                    state = einstein.remove_value(house, 'house_color', 'green', state)
                # If this house DOES NOT have green in its color list
                # THEN the house to thr right cannot have white
                elif not has_green and white_to_right:
                    state = einstein.remove_value(house_to_right, 'house_color', 'white', state)
        return state            

def rule5(state):
    """The green house owner drinks coffee."""
    house = einstein.get_position('green', state)
    if house:
        return einstein.assign_value(house, 'drink', 'coffee', state)
    else:
        return einstein.propose_value('drink', 'coffee', 'house_color', 'green', state)

def rule6(state):
    """The person who plays polo rears birds."""
    return einstein.propose_value('sport', 'polo', 'pet', 'bird', state)

def rule7(state):
    """The owner of the yellow house plays hockey."""
    return einstein.propose_value('house_color', 'yellow', 'sport', 'hockey', state)

def rule8(state):
    """The man living in the house right in the center drinks milk."""
    return einstein.assign_value('3', 'drink', 'milk', state)
    
def rule9(state):
    """The Norwegian lives in the first house."""
    return einstein.assign_value('1', 'nationality', 'norweigen', state)

def rule10(state):
    """The man who plays baseball lives next to the man who keeps cats."""
    baseball_house = einstein.get_position('baseball', state)
    cat_house = einstein.get_position('cat', state)
    if cat_house and baseball_house: #We have assigned these rules already
        return state
    elif cat_house: #We only know where the cat lives
        return einstein.propose_house(einstein.next_of(cat_house), 'sport', 'baseball', state)
    elif baseball_house:#we only know where the baseball lives
        return einstein.propose_house(einstein.next_of(baseball_house), 'pet', 'cat', state)
    else: #We don't know where either the baseball or cat live
        return state

def rule11(state):
    """The man who keeps horses lives next to the one who plays hockey."""
    hockey_house = einstein.get_position('hockey', state)
    horse_house = einstein.get_position('horse', state)
    if horse_house and hockey_house: #We have assigned these rules already
        return state
    elif horse_house: #We only know where the horse lives
        return einstein.propose_house(einstein.next_of(horse_house), 'sport', 'hockey', state)
    elif hockey_house:#we only know where the hockey lives
        return einstein.propose_house(einstein.next_of(hockey_house), 'pet', 'horse', state)
    else: #We don't know where either the hockey or horse live
        return state

def rule12(state):
    """The man who plays billiards drinks beer."""
    return einstein.propose_value('sport', 'billiards', 'drink', 'beer', state)

def rule13(state):
    """The German plays soccer."""
    return einstein.propose_value('nationality', 'german', 'sport', 'soccer', state)

def rule14(state):
    """The Norwegian lives next to the blue house."""
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
    """The man who plays baseball has a neighbor who drinks water."""
    baseball_house = einstein.get_position('baseball', state)
    water_house = einstein.get_position('water', state)
    if baseball_house and water_house: #We have assigned these rules already
        return state
    elif water_house: #We only know where the water lives
        return einstein.propose_house(einstein.next_of(water_house), 'sport', 'baseball', state)
    elif baseball_house:#we only know where the baseball lives
        return einstein.propose_house(einstein.next_of(baseball_house), 'drink', 'water', state)
    else: #We don't know where either the baseball or water live
        return state

def solve(current_state):
    """

    """
    rule_list = [
        rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
        rule9, rule10, rule11, rule12, rule13, rule14, rule15
    ]
    for p_iter in xrange(100):
        pre_rules_state = current_state
        
        for rule in rule_list:
            old_state = current_state
            current_state = einstein.elimination_sweep(rule(current_state))
            
            if current_state != old_state: #something happened
                print '{0} changed state during iteration {1}'.format(rule.__doc__, p_iter)
                
            if einstein.end_solution(current_state):
                return current_state, p_iter
                
        if current_state == pre_rules_state: #nothing happened
            return current_state, p_iter
        else:
            einstein.print_solution(current_state)
            
    return current_state, p_iter
        
           

if __name__ == '__main__':
    state = deepcopy(einstein.START_STATE)
    state, puzzle_iteration = solve(state)
    print "Stopped at iteration {0}".format(puzzle_iteration)
