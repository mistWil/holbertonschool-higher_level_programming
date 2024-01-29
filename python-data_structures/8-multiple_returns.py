#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence:
        _tuple = (len(sentence), sentence[0])
        return tuple(_tuple)

    else:
        return (len(sentence), None)
