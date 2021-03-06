"""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than 
once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

from collections import Counter
def duplicate_count(text):
    # Your code goes here
    """
    1. Convert all the text to lowercase using .lower()
    2. Break down the text into a list of characters using list(__)
    3. Use Counter to convert the list of characters into a dictionary where the key is the character
       and the value is the number of times that character occurs
    4. Now, Use .items() with the to iterate over the key-value pair
    5. As values for Duplicates will be greater than 1 so check for it and increase the counter k to
       get the number of duplicates
    """
    k=0
    for key,v in Counter(list(text.lower())).items():
        if v>1:
            k+=1
    return k
     
