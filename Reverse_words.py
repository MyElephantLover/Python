# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    word = text.split(' ')
    reversed_words = [w[::-1] for w in word]
    return ' '.join(reversed_words)

