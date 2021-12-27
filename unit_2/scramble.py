"""MIDS 1b Unit 2 Exercises"""
from math import ceil, log2


def interleave(str_1, str_2):
    """Return the interleave of two strings of the same length."""

    result = ""
    for index, _char in enumerate(str_1):
        result = result + str_1[index] + str_2[index]
    return result


def scramble(string):
    """Encode a string by bifurcating it and interleaving the two substrings."""

    # The scramble of a single character is the character itself.

    if len(string) == 1:
        return string

    # The string length must be a power of two.
    # First calculate the desired length.
    # Pad the string with "." characters as need be

    target_length = int(pow(2, ceil(log2(len(string)))))
    string = string.ljust(target_length, ".")

    # Divide the string in half and call interleave on the two substrings.

    str_1 = string[: target_length // 2]
    str_2 = string[target_length // 2 :]

    return interleave(scramble(str_1), scramble(str_2))


def main():
    """The driver for scramble."""

    with open("input.txt", "r") as in_file, open("output.txt", "w") as out_file:
        while True:
            line = in_file.readline().strip()
            if not line:
                break
            out_file.write(scramble(line) + "\n")


if __name__ == "__main__":
    main()
