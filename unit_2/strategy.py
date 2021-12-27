def is_hot(state):
    if state < 2:
        return False
    
    if is_hot(state-1) and is_hot(state/2):
        return False

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