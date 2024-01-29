#!/usr/bin/python3
def multiple_returns(sentence):

    if not sentence:
        return None

    _tuple = (len(sentence), sentence[0])
    return tuple(_tuple)
