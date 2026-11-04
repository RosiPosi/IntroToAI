from alphabeta import TicTacToe
from alphabeta import alpha_beta_value


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    while not state.is_end_state():
        print(state)

        children = state.generate_children()

        # Choose the move that is best for the current player.
        best_child = children[0]
        best_value = alpha_beta_value(best_child)

        for child in children[1:]:
            child_value = alpha_beta_value(child)

            if state.is_max_node() and child_value > best_value:
                best_child = child
                best_value = child_value

            elif not state.is_max_node() and child_value < best_value:
                best_child = child
                best_value = child_value

        state = best_child

    print(state)

def main():
    """You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    empty_board = 3 * '???'
    # state = TicTacToe(empty_board, True)
    state = TicTacToe("oxox?x?o?", False)
    print(state)
    play(state)


if __name__ == '__main__':
    main()
