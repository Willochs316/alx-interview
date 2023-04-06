#!/usr/bin/python3

def minOperations(n: int) -> int:
    if n < 1:
        return 0  # Return 0 if n is impossible to achieve
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
