"""
### FILL IN THE GRID PUZZLE

Objective: Arange the numbers 1 through 8 in the grid below.

        +---+---+
        |   |   |
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
        |   |   |
        +---+---+

RULES:
    No consecutive numbers may appear next to each other either vertically, horizontally or diagonally.
    Each number may only be used once.
"""

import grid8

def solve(state):
    """
    Recursive solution that uses a brute force approach to findindg the solution.

    2 essential facts are derived from the board state.
        - The number of empty spaces left.
        - The choice of numbers remaining.

    Solve for a given state
    The base case:
        If no there is no empty spaces the game is over so retrun the end state.
    The recursive case:
        While there are empty spaces, AND while there are choices remaining.
            If you can make a valid assignment,
                then assign the number to the board to create a new state.
                Solve for the new state. <------ Recursion, back to the top with a new step
            Else
                Try another number in this space.
                OR
                None of the numbers fit here so try them in another space.
    Everything failed

    :param dict state: the state of the board
    :return dict: the end state of the game.  None means no solution.
    """
    # uncomment the line below if you would like to see a trace.
    # print state

    # Derive the number of empty spaces left and the choices remaining to go on the board
    empty_spaces = [g for g, v in state.items() if v is None]
    numbers_used = [v for g, v in state.items() if v]
    numbers_left = [n for n in (1,2,3,4,5,6,7,8,) if n not in numbers_used]

    ### BASE CASE
    if not empty_spaces:
        return state

    ### RECURSIVE CASE
    while empty_spaces:
        # Treat the remaining options like a stack
        grid_square = empty_spaces.pop(0) # Grab the next space available
        while numbers_left:
            value = numbers_left.pop(0)   # Grab the next number available

            # If we can make an assignment
            if grid8.assignment_valid(grid_square, value, state):

                # Make a new state by assiging a number
                new_state = grid8.assign_to_grid(grid_square, value, state)
                ### RECURSION
                # Try to solve things from this state
                # Remember, if the base above is returned then this is where we will catch it.
                new_state = solve(new_state)

                if new_state: # return the solution
                    return new_state
                # If the state was none we will implicitly try the remaining numbers or spaces
                # in this branch of the solution tree.

    # No sweat, if this branch is exhausted return None.
    # This may be the last branch meaning the state we started in coudln't be solved.
    return None


if __name__ == "__main__":
    # create a board for printing purposes
    board = """SOLUTION!! :-)
    +---+---+
    | {0} | {1} |
+---+---+---+---+
| {2} | {3} | {4} | {5} |
+---+---+---+---+
    | {6} | {7} |
    +---+---+\n"""

    # Cycle through all the possible starting points to see how many solutions there are.
    for start in (1,2,3,4,5,6,7,8,):
        # Assign a starting point.
        new_state = grid8.assign_to_grid((1, 2,), start, grid8.GRID)
        # try to solve from here
        solution = solve(new_state)

        if solution: # print a solution if we got one
            values = [solution[k] for k in sorted(solution.keys())]
            print board.format(*values)
