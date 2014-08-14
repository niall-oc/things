import unittest
import einstein
from copy import deepcopy

class EinsteinTest(unittest.TestCase):
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
        new_state = einstein.assign_value('1', 'nationality', 'norweigen', einstein.START_STATE)
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
        new_state = einstein.assign_value('1', 'nationality', 'norweigen', einstein.START_STATE)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])
        new_state = einstein.assign_value('1', 'nationality', 'norweigen', new_state)
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
        new_state = einstein.assign_value('1', 'nationality', 'norweigen', einstein.START_STATE)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])
        # We whould see state error on a double assignment
        with self.assertRaises(einstein.StateError):
            new_state = einstein.assign_value('2', 'nationality', 'norweigen', new_state)

    def test_bogus_assignment(self):
        """
        If we attemp to assign a bogus value we gat a KeyError
        """
        with self.assertRaises(KeyError):
            einstein.assign_value('1', 'vehicle', 'car', einstein.START_STATE)

    def test_get_position(self):
        """
        If a value like 'norweigen' or 'dog' is the only value in a set of
        potential values then its been assigned.

        In this case return the house.

        If there is no such case return None
        """
        new_state = deepcopy(einstein.START_STATE)
        # Not assigned so it won't be found
        self.assertIsNone(einstein.get_position('norweigen', new_state))

        # Assign it and we will find it
        new_state = einstein.assign_value('1', 'nationality', 'norweigen', new_state)
        self.assertEqual(new_state['1']['nationality'], set(['norweigen']))
        self.assertEqual(einstein.get_position('norweigen', new_state), '1')

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
        new_state = einstein.deepcopy(einstein.START_STATE)
        new_state['1']['nationality'] = set(['norweigen'])
        new_state = einstein.elimination_sweep(new_state)
        self.assertNotIn('blue', new_state['2']['nationality'])
        self.assertNotIn('blue', new_state['3']['nationality'])
        self.assertNotIn('blue', new_state['4']['nationality'])
        self.assertNotIn('blue', new_state['5']['nationality'])
        ### LOCK
        self.assertEqual(einstein.get_position('norweigen', new_state), '1')

    def test_propose_value(self):
        """
        Proposing a value doesn't officially make an assignment.

        If the Swede keeps a bird then no one else can.
        If the Swede doesn't live in that house then neither can the bird.
        """
        # Proposing a value with no assignments made won't change state
        new_state = deepcopy(einstein.START_STATE)
        new_state = einstein.propose_value('nationality', 'swedish', 'pet', 'bird', new_state)
        self.assertEqual(new_state, einstein.START_STATE)

        # The norweigen cannot own a bird, because the swede does.
        new_state = einstein.assign_value('1', 'nationality', 'norweigen', new_state)
        new_state = einstein.propose_value('nationality', 'swedish', 'pet', 'bird', new_state)
        self.assertNotIn('bird', new_state['1']['pet'])

        # If house 3 owns a horse then the swede cannot live there, because he owns a bird.
        new_state = einstein.assign_value('3', 'pet', 'horse', new_state)
        new_state = einstein.propose_value('nationality', 'swedish', 'pet', 'bird', new_state)
        self.assertNotIn('swedish', new_state['3']['nationality'])

    def test_next_to_houses(self):
        """
        Some rules tell you that next to a house a certain condition is true.

        The white house is to the left of the green house.
        House 2 is to the right of house 1.
        1, 2, 3, 4, 5
        """
        self.assertIsNone(einstein.left_of('1'))
        self.assertIsNone(einstein.right_of('5'))
        self.assertIsNone(einstein.left_of('20'))
        self.assertEqual('1', einstein.left_of('2'))
        self.assertEqual('3', einstein.left_of('4'))
        self.assertEqual('3', einstein.right_of('2'))
        self.assertEqual(['2', '4'], einstein.next_to('3'))
        self.assertEqual(['2'], einstein.next_to('1'))
        self.assertEqual(['4'], einstein.next_to('5'))
