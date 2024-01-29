#!/usr/bin/python3
def multiple_returns(sentence):

    if not sentence:
        return(len(sentence), None)

    _tuple = (len(sentence), sentence[0])
    return tuple(_tuple)
