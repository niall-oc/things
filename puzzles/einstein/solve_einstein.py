import einstein
from copy import deepcopy


def the_person_who_is(predicate, with_this, new_predicate, assign_this, state):
    """
    If the person matches a predicate then assing another predicate.

    eg.  The brit lives in a red house.

    If you find a brit assign the house red.
    Else if you find a red house assign the brit.
    Else propose the following
        If a house has no british posibilities remove red.
        If a house has no red possibilities remove british.

    :param str predicate: The predicate we are looking for.
    :param str with_this: Value to search with.
    :param str predicate: The predicate we will asign.
    :param str assign_this: Value to assign.
    :param dict state: The current state of the universe.
    """
    house_is_this = einstein.get_position(with_this, state)
    house_assigned_this = einstein.get_position(assign_this, state)
    if house_is_this and house_assigned_this:
        return state
    elif house_is_this:
        return einstein.assign_value(house_is_this, new_predicate , assign_this, state)
    elif house_assigned_this:
        return einstein.assign_value(house_assigned_this, predicate, with_this, state)
    else:
        return einstein.propose_link(predicate, with_this, new_predicate, assign_this, state)


def the_neighbour_of(predicate, with_this, new_predicate, can_have_this, state):
    """
    If the house contains a predicate then the neighbouring house can have
    another predicate

    eg.  The man who keeps horses lives next to the one who plays hockey.

    If this house has horses
    THEN next door can have hockeybut not horses
    AND this house cannot have hockey

    :param str predicate: The predicate we are looking for.
    :param str with_this: Value to search with.
    :param str predicate: The predicate we will asign.
    :param str can_have_this: Value to the neighbour can have.
    :param dict state: The current state of the universe.
    """
    found_with_this = einstein.get_position(with_this, state)
    found_have_this = einstein.get_position(can_have_this, state)
    if found_with_this and found_have_this: #We have assigned these rules already
        return state
    elif found_with_this: #We only know where the horse lives
        houses = einstein.next_to(found_with_this)
        if len(houses) == 1:
            return einstein.assign_value(houses[0], new_predicate, can_have_this, state)
        else:
            return einstein.propose_house(houses, new_predicate, can_have_this, state)
    elif found_have_this: #We only know where the hockey is played
        houses = einstein.next_to(found_have_this)
        if len(houses) == 1:
            return einstein.assign_value(houses[0], predicate, with_this, state)
        else:
            return einstein.propose_house(houses, predicate, with_this, state)
    else: #We don't know where either the hockey or horse live
        return state


def rule1(state):
    """The Brit lives in a red house."""
    return the_person_who_is('nationality', 'british', 'house_color', 'red', state)


def rule2(state):
    """The Swede keeps dogs."""
    return the_person_who_is('nationality', 'swedish', 'pet', 'dog', state)


def rule3(state):
    """The Dane drinks tea."""
    return the_person_who_is('nationality', 'danish', 'drink', 'tea', state)


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
                # If this house_color is green
                # BUT the house on the right is not white
                # THEN green must be removed from this house
                if has_green and not white_to_right:
                    state = einstein.remove_value(house, 'house_color', 'green', state)
                # If this house is NOT green
                # THEN the house to the right cannot be white
                elif not has_green and white_to_right:
                    state = einstein.remove_value(house_to_right, 'house_color', 'white', state)
        return state


def rule5(state):
    """The green house owner drinks coffee."""
    return the_person_who_is('drink', 'coffee', 'house_color', 'green', state)


def rule6(state):
    """The person who plays polo rears birds."""
    return the_person_who_is('sport', 'polo', 'pet', 'bird', state)


def rule7(state):
    """The owner of the yellow house plays hockey."""
    return the_person_who_is('house_color', 'yellow', 'sport', 'hockey', state)


def rule8(state):
    """The man living in the house right in the center drinks milk."""
    if einstein.get_position('milk', state): # Don't set twice
        return state
    else:
        return einstein.assign_value('3', 'drink', 'milk', state)


def rule9(state):
    """The Norwegian lives in the first house."""
    if einstein.get_position('norweigen', state): # Don't set twice
        return state
    else:
        return einstein.assign_value('1', 'nationality', 'norweigen', state)


def rule10(state):
    """The man who plays baseball lives next to the man who keeps cats."""
    return the_neighbour_of('sport', 'baseball', 'pet', 'cat', state)


def rule11(state):
    """The man who keeps horses lives next to the one who plays hockey."""
    return the_neighbour_of('pet', 'horse', 'sport', 'hockey', state)


def rule12(state):
    """The man who plays billiards drinks beer."""
    return the_person_who_is('sport', 'billiards', 'drink', 'beer', state)


def rule13(state):
    """The German plays soccer."""
    return the_person_who_is('nationality', 'german', 'sport', 'soccer', state)


def rule14(state):
    """The Norwegian lives next to the blue house."""
    return the_neighbour_of('nationality', 'norweigen', 'house_color', 'blue', state)


def rule15(state):
    """The man who plays baseball has a neighbor who drinks water."""
    return the_neighbour_of('sport', 'baseball', 'drink', 'water', state)


def solve(current_state, rule_order):
    """
    Solve the puzzle with a list of rules
    """
    iteration = 1
    while not einstein.end_solution(current_state):
        # Safe guard to ensure a rules are being applied
        pre_rules_state = current_state
        print("######  begin iteration", iteration)
        for rule in rule_order:
            old_state = current_state

            # See what changes state
            current_state = rule(current_state)
            if current_state != old_state: #something happened
                print('RULE {0} changed state'.format(rule.__doc__))

            # see if any additional changes can be made
            current_state = einstein.elimination_sweep(current_state)

        # Safe guard to ensure a rules are being applied
        if current_state == pre_rules_state: #nothing happened
            break
        iteration += 1
    return current_state, iteration - 1

if __name__ == '__main__':
    state = deepcopy(einstein.START_STATE)
    rule_order = [
        rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
        rule9, rule10, rule11, rule12, rule13, rule14, rule15
    ]
    state, iteration = solve(state, rule_order)
    einstein.print_solution(state)
    print('\n\nSolved: {0} on iteration {1}'.format(einstein.end_solution(state), iteration))
