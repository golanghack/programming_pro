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
    list_punctuation = ['.', '!', '?', '`']
    position = 0 

    while position < len(get_string) and get_string[position] == ' ':
        position += 1
    
    if position < len(get_string):
        # replace symbol to Capitalize
        get_string = (get_string[0: position] + 
                            get_string[position].upper() +
                            get_string[position + 1: len(get_string)])

    # for !, ?, . 
    while position < len(get_string):
        if get_string[position] in list_punctuation:
            position += 1
            while position < len(get_string) and get_string[position] == ' ':
                position += 1
        
        if position < len(get_string):
            get_string = (get_string[0: position] + 
                                get_string[position].upper() + 
                                get_string[position + 1: len(get_string)])
    
    # next symbol 
    #position += 1

    position = 1 
    while position < len(get_string) - 1:
        if (get_string[position - 1] == ' ' and 
            get_string[position] == 'i' and 
            get_string[position + 1] == ' ' or 
            get_string[position + 1] in list_punctuation):
            # replace i on I 
            get_string = (get_string[0: position] + 
                        'I' + 
                        get_string[position + 1: len(get_string)])
        position += 1
    return get_string

def main():
    print(capitalizer('Enter string -> '))

if __name__ == '__main__':
    main()