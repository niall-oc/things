from   copy import deepcopy
import logging


house_colors =  ['red',     'green',  'blue',     'white',   'yellow']
nationalities = ['british', 'danish', 'german',   'swedish', 'norweigen']
drinks =        ['tea',     'coffee', 'milk',     'beer',    'water']
sports =        ['polo',    'hockey', 'baseball', 'soccer',  'billiards']
pets =          ['dog',     'cat',    'horse',    'bird',    'fish']


START_STATE = {
    '1': {'house_color': set(house_colors), 'nationality': set(nationalities),
        'drink': set(drinks), 'sport': set(sports), 'pet': set(pets)},
    '2': {'house_color': set(house_colors), 'nationality': set(nationalities),
        'drink': set(drinks), 'sport': set(sports), 'pet': set(pets)},
    '3': {'house_color': set(house_colors), 'nationality': set(nationalities),
        'drink': set(drinks), 'sport': set(sports), 'pet': set(pets)},
    '4': {'house_color': set(house_colors), 'nationality': set(nationalities),
        'drink': set(drinks), 'sport': set(sports), 'pet': set(pets)},
    '5': {'house_color': set(house_colors), 'nationality': set(nationalities),
        'drink': set(drinks), 'sport': set(sports), 'pet': set(pets)},
}

class StateError(Exception):
    pass

def print_solution(state):
    """
    A very simple print function to show the current solution .
    
    :param dict state: The state of the world.
    """
    print '\n\n'
    row = "{0:13s} | {1:13s}| {2:13s}| {3:13s}| {4:13s}| {5:13s}|"
    new_state = deepcopy(state)
    get_property = lambda ps: ps.pop() if len(ps) == 1 else 'unknown'
    for property in ('house_color', 'nationality', 'drink', 'sport', 'pet',):
        print row.format(
            property,
            get_property(new_state['1'][property]),
            get_property(new_state['2'][property]),
            get_property(new_state['3'][property]),
            get_property(new_state['4'][property]),
            get_property(new_state['5'][property])
        )

def remove_value(position, property, value, state):
    """
    Remove a value from a houses property set.

    :param str position: The key in the state dictionary identifying the house.
    :param str property: The property in state[position] being updated.
    :param str value: value is assigned to state[position][property].
    :param dict state: The current state of the world.
    :return dict: The new state of world.
    """
    new_state = deepcopy(state)
    try:
        new_state[position][property].remove(value)
    except KeyError:
        logging.warning("Value %s can't be removed from %s", value, property)
    finally:
        if not new_state[position][property]:
            raise StateError("House %s, %s no values left!", position, property)
    return new_state

def assign_value(position, property, value, state):
    """
    Updates a house's property to be a single value.  
    Eliminates that value from the same property set in other houses.
    
     - The norweigen lives in the first house.
    
    Therefore he cannot live in any other houses.

    :param str position: The key in the state dictionary identifying the house.
    :param str property: The property in state[position] being updated.
    :param str value: value is assigned to state[position][property].
    :param dict state: The current state of the world.
    :return dict: The new state of world.
    """
    new_state = deepcopy(state)
    new_state[position][property] = set([value])
    for house, details in new_state.iteritems():
        if house != position:
            new_state = remove_value(house, property, value, new_state)
    return new_state

def get_position(value, state):
    """
    Return the house where a specific value has been assigned to a property.
    Assignment is true when that value is the only member of the set of possible
    values for that property.

    :param str value: The value you are searching for.
    :param dict state: The current state of the universe.
    :return str or None: The key representing the house or None.
    """
    for house, properties in state.iteritems():
        for property, values in properties.iteritems():
            if value in values and len(values) == 1:
                return house
    return None

def left_of(house):
    """
    Find the house to the left of this house.
    
    :param str house: the key of the house we are looking at.
    """
    left = str(int(house)-1)
    return left if left in START_STATE.keys() else None

def right_of(house):
    """
    Find the house to the right of this house.
    
    :param str house: the key of the house we are looking at.
    """
    right = str(int(house)+1)
    return right if right in START_STATE.keys() else None

def next_to(house):
    """
    Find the houses either side of this house.
    
    :param str house: the key of the house we are looking at.
    """
    return  [h for h in (left_of(house), right_of(house),) if h]

def last_man_standing(state):
    """
    Generator to find assigned values. There are cases where several assignments
    leave only one posibility for a property of a house. This is the last man 
    standing rule. Essentially this is an implicit assignment.

    :param dict state: The state of the universe.
    :return dict or None: The house or None.
    :yield tuple: (house, property, value)
    """
    for house, properties in state.iteritems():
        for property, values in properties.iteritems():
            if len(values) == 1:
                yield (house, property, tuple(values)[0],)

def elimination_sweep(state):
    """
    Traverse the state and assert that anything discovered by the last man 
    standing rule is correctly assigned.
    
    :param dict state: The state of the universe.
    """
    new_state = deepcopy(state)
    for house, property, value in last_man_standing(state):
        new_state = assign_value(house, property, value, new_state)
    return new_state

def propose_value(assignee_property, assignee_value, assignment_property, assignment_value, state):
    """
    Only the assignee can have this assignment.

    If a Swede keeps a bird then no one else can.

    :param assignee_property: The owner property eg 'nationality'
    :param assignee_value: The owner value eg 'Swede'
    :param assignment_property: The assignment property eg 'pet'
    :param assignment_value: The assignment value eg 'bird'
    :param dict state: The state of the universe.
    """
    new_state = deepcopy(state)
    for house, properties in new_state.iteritems(): # In this house
        for property, values in properties.iteritems(): # Examine the properties

            if assignee_property == property: # If the property nationality
                if assignee_value not in values: # But its not the Swede
                    # Then remove the bird from the set of pets in this house.
                    new_state = remove_value(house, assignment_property, assignment_value, new_state)

            if assignment_property == property: # If the property is the pet
                if len(values) == 1: # and only one pet is set
                    if assignment_value not in values: # and the pet is not a bird
                        # Then the Swede cannot live in this house.
                        new_state = remove_value(house, assignee_property, assignee_value, new_state)
    return new_state

def propose_house(positions, property, value, state):
    """
    Proposing a specific house has a property means no other house can have it.
    
     - The house nest to the green house is white.
    
    This means we should ensure white remains in the house_color set for any
    house nest to the green one.
    And ensure white is removed from all other house_color sets.

    :param list positions: Keys in the state dictionary identifying the house.
    :param str property: The property in state[position] being updated.
    :param str value: value is assigned to state[position][property].
    :param dict state: The current state of the world.
    :return dict: The new state of world.
    """
    new_state = deepcopy(state)
    for house, properties in new_state.iteritems(): # In this house
        if house not in positions:
            new_state = remove_value(house, property, value, new_state)
    return new_state

def end_solution(state):
    """
    If every property set has only 1 value left then we have solved the puzzle.
    
    :param dict state: The current state of the world.
    """
    for house, properties in state.iteritems(): # In this house
        for property, values in properties.iteritems(): # Examine the properties
            if len(values) > 1:
                return False
    return True
