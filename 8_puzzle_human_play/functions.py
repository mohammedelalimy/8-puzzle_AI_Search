def get_actions(puzzle):
    # Returns a list of all available moves
    moves = {0: ['>', 'v'], 1: ['<', '>', 'v'], 2: ['<', 'v'],
                  3: ['^', '>', 'v'], 4: ['^', '<', '>', 'v'], 5: ['^', '<', 'v'],
                  6: ['^', '>'], 7: ['^', '<', '>'], 8: ['^', '<']}
    empty_cell = puzzle.index(0)
    moves = [move for move in moves[empty_cell] if move in ['<', '>', '^', 'v']]
    return moves


def implement_action(action, puzzle):
    # Apply given action to puzzle state and returns a new state for puzzle.
    offsets = {'<': -1, '>': 1, '^': -3, 'v': 3}
    empty_cell = puzzle.index(0)
    new_index = empty_cell + offsets.get(action, 0)
    if new_index < 0 or new_index >= len(puzzle):
        return puzzle  # Invalid
    new_state = puzzle[:]
    new_state[empty_cell], new_state[new_index] = new_state[new_index], new_state[empty_cell]
    return new_state


def checking(puzzle):
    # Checks if the puzzle is solved and returns True if so, False otherwise.
    return all(puzzle[i] == i for i in range(9))
