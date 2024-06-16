#!/usr/bin/python3
'''
Minimal Operations
'''


def minOperations(n):
    '''
    a script to check minimal operations to copy and paste n number of times
    ARGS:
        one arg n

    RETURNS:
        the operation count
    '''
    if not isinstance(n, int) or n < 1:
        return 0

    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if n % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        else:
            done += clipboard
            ops_count += 1

    return ops_count
