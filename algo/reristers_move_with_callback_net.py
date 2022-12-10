#! /usr/bin/env python3 

"""<--ALGO -> REGISTERS MOVE WITH CALLBACK LINEAR NET-->"""

def callback_linear_shift(bits: list) -> list:
    """Return pseudo sporadic byte and new state bits list"""
    
    xor_result = (bits[1] + bits[2]) % 2
    out = bits.pop()
    bits.insert(0, xor_result)
    return bits, out

def callback_linear_shift_list(bits: list) -> list:
    """Generator of list output bits
    
    >>> bts_list = callback_linear_shift_list([1, 1, 1])[0]
    >>> print(bts_list)
    [[1, 1, 1], [0, 1, 1], [0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    >>> print(callback_linear_shift_list([1, 1, 1])[1])
    [1, 1, 1, 0, 0, 1, 0]
    """
    
    out = [bits.copy()]
    random_out = []
    next_bit = bits.copy()
    while (len(out) < 2 ** len(bits)):
        next_bit, next_ = callback_linear_shift(next_bit)
        out.append(next_bit.copy())
        random_out.append(next_)
    return out, random_out

if __name__ == '__main__':
    import doctest
    doctest.testmod()
  