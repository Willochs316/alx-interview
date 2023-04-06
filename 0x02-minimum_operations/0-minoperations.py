#!/usr/bin/python3
'''
The minimum operations coding challenge.
'''


def minOperations(n: int) -> int:
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int) or n < 1:
        return -1  # Return an error code for invalid input
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            # Initialize by copying one character
            clipboard = done
            ops_count += 1
        elif n % done == 0:
            # Paste and repeat until target is reached
            clipboard = done
            done += clipboard
            ops_count += 1
        else:
            # Paste
            done += clipboard
            ops_count += 1
    return ops_count
