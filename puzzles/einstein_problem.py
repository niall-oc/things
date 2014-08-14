from   copy import deepcopy
import logging
import unittest2 as unittest

logger = logging.getLogger(__name__)

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

def print_state(new_state):
    print '\n\n'
    row = "{5:13s} | {0:13s}| {1:13s}| {2:13s}| {3:13s}| {4:13s}|"
    state = deepcopy(new_state)
    for property in ('house_color', 'nationality', 'drink', 'sport', 'pet',):
        print row.format(
            state['1'][property].pop() if len(state['1'][property]) < 2 else 'unknown',
            state['2'][property].pop() if len(state['2'][property]) < 2 else 'unknown',
            state['3'][property].pop() if len(state['3'][property]) < 2 else 'unknown',
            state['4'][property].pop() if len(state['4'][property]) < 2 else 'unknown',
            state['5'][property].pop() if len(state['5'][property]) < 2 else 'unknown',
            property
        )

def remove_value(house, property, value, state):
    """
    Remove a value from a houses property set.

    :param str house: The key in the state dictionary identifying the house.
    :param str property: The property state[house_position] that will be updated.
    :param str value: The value at state[house_position][property] that will be updated.
    :param dict state: The state of the world.
    
    :return dict: Updates state of the universe
    """
    new_state = deepcopy(state)
    try:
        new_state[house][property].remove(value)
    except KeyError:
        logger.warning("Value {0} was not in {1}".format(value, new_state[house][property]))
    finally:
        if not new_state[house][property]:
            raise StateError("House {0} - {1} has no values left!".format(house, property))
    return new_state

def assign_value(house_position, property, value, state):
    """
    Updates a house's property to be a single value.  Eliminates that value from
    any possible states for other houses.

    :param str house_position: The key in the state dictionary identifying the house.
    :param str property: The property state[house_position] that will be updated.
    :param str value: The value at state[house_position][property] that will be updated.
    :param dict state: The state of the world.
    :return dict: New state of world.
    """
    new_state = deepcopy(state)
    new_state[house_position][property] = set([value])
    for house, details in new_state.iteritems():
        if house != house_position:
            new_state = remove_value(house, property, value, new_state)
    return new_state

def get_house(value, state):
    """
    Return the house where a specific value has been assigned to a property.
    Assignment is true when that value is the only member of the set
    of possible values for that property.

    :param str value: The value you are searching for.
    :param dict state: The state of the universe.
    :return str or None: The key representing the house or None.

    usage:
        get_value('Swede', state)
        None
        get_value('Norweigen', state)
        '1'
    """
    for house, properties in state.iteritems():
        for property, values in properties.iteritems():
            if value in values and len(values) == 1:
                return house
    return None

def left_of(house):
    left = str(int(house)-1)
    return left if left in START_STATE.keys() else None

def right_of(house):
    right = str(int(house)+1)
    return right if right in START_STATE.keys() else None

def next_to(house):
    return  [h for h in (left_of(house), right_of(house),) if h]

def last_man_standing(state):
    """
    Generator to find assigned values.  There are cases where several assignments leave
    only one posibility for a property of a house.  The is the last man standing rule.
    Essentially this is an implicit assignment.

    :param dict state: The state of the universe.
    :return dict or None: The house or None.
    :yield tuple: (house, property, value)
    """
    for house, properties in state.iteritems():
        for property, values in properties.iteritems():
            if len(values) == 1:
                yield (house, property, tuple(values)[0],) # grab a copy of that value

def elimination_sweep(state):
    """
    Traverse the state and assert that anything discovered by the last man standing rule
    is correctly assigned.
    """
    new_state = deepcopy(state)
    assignments = last_man_standing(state)
    for house, property, value in assignments:
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

def propose_house(house_positions, property, value, state):
    """
    Updates a house's property to be a single value.  Eliminates that value from
    any possible states for other houses.

    :param str house_position: The key in the state dictionary identifying the house.
    :param str property: The property state[house_position] that will be updated.
    :param str value: The value at state[house_position][property] that will be updated.
    :param dict state: The state of the world.
    :return dict: New state of world.
    """
    new_state = deepcopy(state)
    for house, properties in new_state.iteritems(): # In this house
        if house not in house_positions:
            new_state = remove_value(house, property, value, new_state)
    return new_state


class EinsteinPuzzle(unittest.TestCase):
    """
    We need to assert who owns the Fish.

    1  The Brit lives in a red house
    2  The Swede keeps dogs
    3  The Dane drinks tea
    4  The green house is on the left of the white house
    5  The green house owner drinks coffee
    6  The person who plays polo rears birds
    7  The owner of the yellow house plays hockey
    8  The man living in the house right in the center drinks milk
    9  The Norwegian lives in the first house
    10 The man who plays baseball lives next to the man who keeps cats
    11 The man who keeps horses lives next to the one who plays hockey
    12 The man who plays billiards drinks beer
    13 The German plays soccer
    14 The Norwegian lives next to the blue house
    15 The man who plays baseball has a neighbor who drinks water
    """
    def test_assign_norweigen_to_first_house(self):
        """
        Assert rule 9 the norweigen lives in the first house.
        """
        # How do we represent this rule using a step from one state to the next
        # assign_value('1', 'nationality', 'norweigen', START_STATE)
        new_state = assign_value('1', 'nationality', 'norweigen', START_STATE)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])

    def test_duplicate_assignment(self):
        """
        If we make the same assignment twice it won't cause a problem.
        We will however like to see a message logged.
        """
        new_state = assign_value('1', 'nationality', 'norweigen', START_STATE)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])
        new_state = assign_value('1', 'nationality', 'norweigen', new_state)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])

    def test_double_assignment(self):
        """
        If we attempt to assign the same value to two places we have gone
        wrong and should raise an error.
        """
        new_state = assign_value('1', 'nationality', 'norweigen', START_STATE)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])
        # We whould see state error on a double assignment
        with self.assertRaises(StateError):
            new_state = assign_value('2', 'nationality', 'norweigen', new_state)

    def test_bogus_assignment(self):
        """
        If we attemp to assign a bogus value we gat a KeyError
        """
        with self.assertRaises(KeyError):
            assign_value('1', 'vehicle', 'car', START_STATE)

    def test_get_house(self):
        """
        If a value like 'norweigen' or 'dog' is the only value in a set of
        potential values then its been assigned.

        In this case return the house.

        If there is no such case return None
        """
        new_state = deepcopy(START_STATE)
        # Not assigned so it won't be found
        self.assertIsNone(get_house('norweigen', new_state))

        # Assign it and we will find it
        new_state = assign_value('1', 'nationality', 'norweigen', new_state)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertEqual(get_house('norweigen', new_state), '1')

        # It also won't feature anywhere else
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])

    def test_elimination_sweep(self):
        """
        If a set of values dwindles to just one value then the last_man_standing rule applies.

        In this case officially assigning the value will correct state
        """
        new_state = deepcopy(START_STATE)
        new_state['1']['nationality'] = set(['norweigen'])
        new_state = elimination_sweep(new_state)
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])
        ### LOCK
        self.assertEqual(get_house('norweigen', new_state), '1')

    def test_propose_value(self):
        """
        Proposing a value doesn't officially make an assignment.

        If the Swede keeps a bird then no one else can.
        If the Swede doesn't live in that house then neither can the bird.
        """
        # Proposing a value with no assignments made won't change state
        new_state = deepcopy(START_STATE)
        new_state = propose_value('nationality', 'swedish', 'pet', 'bird', new_state)
        self.assertEqual(new_state, START_STATE)

        # The norweigen cannot own a bird, because the swede does.
        new_state = assign_value('1', 'nationality', 'norweigen', new_state)
        new_state = propose_value('nationality', 'swedish', 'pet', 'bird', new_state)
        self.assertNotIn('bird', new_state['1']['pet'])

        # If house 3 owns a horse then the swede cannot live there, because he owns a bird.
        new_state = assign_value('3', 'pet', 'horse', new_state)
        new_state = propose_value('nationality', 'swedish', 'pet', 'bird', new_state)
        self.assertNotIn('swedish', new_state['3']['nationality'])

    def test_next_to_houses(self):
        """
        Some rules tell you that next to a house a certain condition is true.

        The white house is to the left of the green house.
        House 2 is to the right of house 1.
        1, 2, 3, 4, 5
        """
        self.assertIsNone(left_of('1'))
        self.assertIsNone(right_of('5'))
        self.assertIsNone(left_of('20'))
        self.assertEqual('1', left_of('2'))
        self.assertEqual('3', left_of('4'))
        self.assertEqual('3', right_of('2'))
        self.assertEqual(['2', '4'], next_to('3'))
        self.assertEqual(['2'], next_to('1'))
        self.assertEqual(['4'], next_to('5'))


def main():
    suite = unittest.TestSuite()
    suite.addTest(EinsteinPuzzle('test_next_to_houses'))
    suite.addTest(EinsteinPuzzle('test_propose_value'))
    unittest.TextTestRunner().run(suite)
    # return
    # 4  The Brit lives in a red house
    # 5  The Swede keeps dogs
    # 6  The Dane drinks tea
    # -  The green house is on the left of the white house
    # 7  The green house owner drinks coffee
    # 10 The person who plays polo rears birds
    # -  The owner of the yellow house plays hockey
    # 3  The man living in the house right in the center drinks milk
    # 1  The Norwegian lives in the first house
    # -- The man who plays baseball lives next to the man who keeps cats
    # -- The man who keeps horses lives next to the one who plays hockey
    # 9  The man who plays billiards drinks beer
    # 8  The German plays soccer
    # 2  The Norwegian lives next to the blue house
    # -- The man who plays baseball has a neighbor who drinks water
    from pprint import pprint

    new_state = assign_value('1', 'nationality', 'norweigen', START_STATE)
    houses = next_to(get_house('norweigen', new_state))
    if len(houses) > 1:
        new_state = propose_house(houses, 'house_color', 'blue', new_state)
    else:
        new_state = assign_value(houses[0], 'house_color', 'blue', new_state)
    new_state = elimination_sweep(new_state)
    new_state = assign_value('3', 'drink', 'milk', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('house_color', 'red', 'nationality', 'british', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('nationality', 'swedish', 'pet', 'dog', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('nationality', 'danish', 'drink', 'tea', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('house_color', 'green', 'drink', 'coffee', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('nationality', 'german', 'sport', 'soccer', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('sport', 'billiards', 'drink', 'beer', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('sport', 'polo', 'pet', 'bird', new_state)
    new_state = elimination_sweep(new_state)
    new_state = propose_value('sport', 'polo', 'pet', 'bird', new_state)
    new_state = elimination_sweep(new_state)s


    pprint(new_state)
    print_state(new_state)
