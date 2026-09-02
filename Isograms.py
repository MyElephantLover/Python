# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    # Convert the string to lowercase to ignore case
    string = string.lower()
    # Create a set to track seen letters
    seen_letters = set()
    
    for letter in string:
        # Check if the letter is already in the set
        if letter in seen_letters:
            return False  # Not an isogram if letter is repeated
        seen_letters.add(letter)  # Add the letter to the set
    
    return True  # Return True if no letters are repeated