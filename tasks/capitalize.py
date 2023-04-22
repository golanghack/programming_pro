#! /usr/bin/env python3 

"""TASK 
Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. To help address this situation, you will create a function
that takes a string as its only parameter and returns a new copy of the string that has
been correctly capitalized. In particular, your function must:
• Capitalize the first non-space character in the string,
• Capitalize the first non-space character after a period, exclamation mark or question
mark, and
• Capitalize a lowercase “i” if it is preceded by a space and followed by a space,
period, exclamation mark, question mark or apostrophe.
Implementing these transformations will correct most capitalization errors. For
example, if the function is provided with the string “what time do i have to be there?
what’s the address? this time i’ll try to be on time!” then it should return the string
“What time do I have to be there? What’s the address? This time I’ll try to be on
time!”. Include a main program that reads a string from the user, capitalizes it using
your function, and displays the result.
"""

def capitalizer(message: str) -> str:
    """Capitalizer for first letters."""

    get_string = input(message)
    for letter in get_string:
        if letter == ' ':
            
    