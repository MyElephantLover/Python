# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    # Covert the number to a string to access its digits
    num_str = str(num)
    # Sort the digits in descending order and join them back into a string
    sorted_num_str = ''.join(sorted(num_str, reverse=True))
    # Convert the sorted string back to an integer and return it
    return int(sorted_num_str)