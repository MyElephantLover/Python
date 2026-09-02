# Description:
# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the argument is itself not a perfect square then return either -1 or an empty value like None or null, depending on your language. You may assume the argument is non-negative.

def find_next_square(sq):
    # Check if the input is a perfect square
    if sq < 0:
        return -1  # Return None for negative numbers
    root = int(sq**0.5) # raise to the power of 0.5 to get the square root
    if root * root != sq:
        return -1  # Return None if not a perfect square
    # Calculate the next perfect square
    next_root = root + 1
    return next_root * next_root