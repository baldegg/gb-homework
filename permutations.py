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


"""Accepts a single string and appends to permutations list all unique permutations.  
By default, starts iterating at the start of string; start value is only changed when the function is called
recursively."""
def permute(string, start=0):
    # If we are starting from the beginning (ie not being called by recursion), re-initialize our array of permutations
    # so that we don't include permutation sets of previous strings.
    if start == 0:
        permutations.clear()

    # If we are starting at the end of the string, this means we have reached the bottom of a recursion branch.
    # Therefore, we have completed one of our permutations and add it to our list.
    if start == len(string):
        permutations.append(''.join(string))

    # Otherwise, iterate through the string, swapping characters at starting point and iteration counter.
    else:
        for i in range(start, len(string)):
            string[start], string[i] = string[i], string[start]
            # Recursively call the permutation function on the mutated string starting at one place to the right
            # of the current loop. In this manner, every character is swapped with every other character as the start
            # counter approaches the end of the string.
            permute(string, start + 1)
            # We then swap the character back so we can continue iterating through the unmutated string once
            # the recursion calls complete.
            string[start], string[i] = string[i], string[start]


if __name__ == "__main__":
    # Checks that we specify filename and attempts to load it, otherwise reminds of usage.
    if len(sys.argv) == 2:
        infile = sys.argv[1]
        strings = loadFile(infile)
        # Runs permute on output of permute function on each line of file.
        for string in strings:
            # We use python's sorted function on each string before sending it to the permute function because it is
            # less expensive to sort a single string than a possibly huge list of permutations.
            # We want the final list to be sorted ascending 0-9, A-Z, a-z.  Luckily this corresponds to ASCII byte
            # values, which the sorted function uses to sort, so we can just use it directly.
            permute(sorted(string))
            # Swap the last two permutations because they are out of order.
            permutations[-2], permutations[-1] = permutations[-1], permutations[-2]
            # For every iteration, we print the contents of the permutation list joined by commas because it gets
            # wiped when the next string is fed to the permute function.  We sort once more to ensure the last
            # elements are sorted.
            print(','.join(permutations))
    else:
        print("Usage: Specify a filename containing line-separated strings to permute.")

