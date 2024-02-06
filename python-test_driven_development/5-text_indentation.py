#!/usr/bin/python3


"""
Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after.

    Args:
        text (str): The text to be printed
    Raises:
        TypeError: If text is not a string
    Returns:
        _type_: The text with 2 new lines after
    """
    
    new_text = ''
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in text:
        if i == ' ' and len(new_text) == 0:
            continue
        elif i == ' ' and new_text[-1] in '\n':
            continue
        new_text += i
        if i in ".?:":
            new_text += "\n\n"
    print(new_text, end="")
