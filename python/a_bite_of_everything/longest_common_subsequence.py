#! /usr/bin/env python3 

# lcs -> longest common subsequence
def lcs(X: str, Y: str) -> str:
    if X == '' or Y == '':
        return ''
    if X[-1] == Y[-1]:
        return lcs(X[:-1], Y[:-1]) + X[-1]
    else:
        return max([lcs(X[:-1], Y), lcs(X, Y[:-1])], key=len)