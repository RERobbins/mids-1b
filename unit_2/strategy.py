def is_hot(state):
    """Returns True if state is "hot", by which we mean that at least one of
    the player's alternatives places the opponent in a no-win scenario.  The function
    returns False if both alternatives give the opponent a chance to win.
    
    The alternatives are to reduce state by one or divide it in half.
    
    The player that decreases the state number below one loses."""

    # Base case, states is less than two, this player will lose.
    if state < 2:
        return False
    
    # Analyze both alternatives, if neither is how, this state is cold.
    if is_hot(state-1) and is_hot(state/2):
        return False

    # The only way to get to this point is if one alternative is hot.
    return True

def main():
    """The driver for strategy."""

    with open("input.txt", "r") as in_file, open("output.txt", "w") as out_file:
        while True:
            line = in_file.readline().strip()
            if not line:
                break

            if is_hot(int(line)):
                 result="hot"
            else:
                result="cold"

            out_file.write(result + "\n")


if __name__ == "__main__":
    main()