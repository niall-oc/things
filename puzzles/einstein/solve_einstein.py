import einstein

def solve():
    """
    4  The Brit lives in a red house
    5  The Swede keeps dogs
    6  The Dane drinks tea
    -  The green house is on the left of the white house
    7  The green house owner drinks coffee
    10 The person who plays polo rears birds
    -  The owner of the yellow house plays hockey
    3  The man living in the house right in the center drinks milk
    1  The Norwegian lives in the first house
    -- The man who plays baseball lives next to the man who keeps cats
    -- The man who keeps horses lives next to the one who plays hockey
    9  The man who plays billiards drinks beer
    8  The German plays soccer
    2  The Norwegian lives next to the blue house
    -- The man who plays baseball has a neighbor who drinks water
    """
    from pprint import pprint

    new_state = einstein.assign_value('1', 'nationality', 'norweigen', einstein.START_STATE)
    houses = einstein.next_to(einstein.get_position('norweigen', new_state))
    if len(houses) > 1:
        new_state = einstein.propose_house(houses, 'house_color', 'blue', new_state)
    else:
        new_state = einstein.assign_value(houses[0], 'house_color', 'blue', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.assign_value('3', 'drink', 'milk', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('house_color', 'red', 'nationality', 'british', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('nationality', 'swedish', 'pet', 'dog', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('nationality', 'danish', 'drink', 'tea', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('house_color', 'green', 'drink', 'coffee', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('nationality', 'german', 'sport', 'soccer', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('sport', 'billiards', 'drink', 'beer', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('sport', 'polo', 'pet', 'bird', new_state)
    new_state = einstein.elimination_sweep(new_state)
    new_state = einstein.propose_value('sport', 'polo', 'pet', 'bird', new_state)
    new_state = einstein.elimination_sweep(new_state)

    pprint(new_state)
    einstein.print_solution(new_state)

if __name__ == '__main__':
    solve()
