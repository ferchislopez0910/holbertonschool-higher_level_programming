#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if ln == 0:
        sentence = None
    else:
        sentence = sentence[0]
    return(ln, sentence)
