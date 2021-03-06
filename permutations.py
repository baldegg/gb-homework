import sys  # To use sys.argv to read command line arguments

permutations = []  # Initialize list of permutations

"""Loads file from command line argument.  Prints error and exits if file not found.  Otherwise,
reads file line by line and returns list of strings to be to be permuted."""
def loadFile(file):
    try:
        with open(file, 'r') as f:
            lines = f.read().splitlines()
        return lines
    except FileNotFoundError:
        print("File not found.")
        exit(-1)


"""Accepts a list of chars and appends to permutations list all unique permutations.  
By default, starts iterating at the start of string; start value is only changed when the function is called
recursively."""
def permute(chars, start=0):
    # If we are starting from the beginning (ie not being called by recursion), re-initialize our array of permutations
    # so that we don't include permutation sets of previous strings.
    if start == 0:
        permutations.clear()

    # If we are starting at the end of the string, this means we have reached the bottom of a recursion branch.
    # Therefore, we have completed one of our permutations and add it to our list.
    if start == len(chars):
        permutations.append(''.join(chars))

    # Otherwise, iterate through the string, swapping characters at starting point and iteration counter.
    else:
        for i in range(start, len(chars)):
            chars[start], chars[i] = chars[i], chars[start]
            # Recursively call the permutation function on the mutated string starting at one place to the right
            # of the current loop. In this manner, every character is swapped with every other character as the start
            # counter approaches the end of the string.
            permute(chars, start + 1)
            # We then swap the character back so we can continue iterating through the unmutated string once
            # the recursion calls complete.
            chars[start], chars[i] = chars[i], chars[start]


if __name__ == "__main__":
    # Checks that we specify filename and attempts to load it, otherwise reminds of usage.
    if len(sys.argv) == 2:
        infile = sys.argv[1]
        strings = loadFile(infile)
        # Runs permute on output of permute function on each line of file.
        for string in strings:
            # We want the final list to be sorted ascending 0-9, A-Z, a-z.  Luckily this corresponds to ASCII byte
            # values, which the sorted function uses to sort, so we can just use it directly.
            # We presort the string to convert it into a list of chars and reduce sorting time in the final sort.
            permute(sorted(string))
            # For every iteration, we print the contents of the permutation list joined by commas because it gets
            # wiped when the next string is fed to the permute function.  We sort once more to ensure the last
            # elements are sorted.
            print(','.join(sorted(permutations)))
    else:
        print("Usage: Specify a filename containing line-separated strings to permute.")

