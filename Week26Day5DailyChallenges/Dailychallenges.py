#Challenge 1: Sorting
#To solve the sorting problem, you can write a Python program that accepts a comma-separated sequence of words, splits them into a list, sorts them alphabetically, and then prints them back as a comma-separated sequence.


def sort_words():

    input_str = input("Enter a comma-separated sequence of words: ")

    
    words = input_str.split(',')

    
    sorted_words = sorted(words)

    
    print(','.join(sorted_words))

# Fuction to call programme
sort_words()


#Challenge 2: Longest Word
#For this challenge, you need to write a function that finds the longest word in a sentence. The function should return the first longest word if there are multiple words of the same length.


def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Find the longest word
    longest = max(words, key=len)

    return longest

# Test cases
print(longest_word("Margaret's toy is a pretty doll."))  # ➞ "Margaret's"
print(longest_word("A thing of beauty is a joy forever."))  # ➞ "forever."
print(longest_word("Forgetfulness is by all means powerless!"))  # ➞ "Forgetfulness"