#!/usr/bin/python3
"""
lockboxes algorithm
check if all boxes can be unlocked
return true or false
"""


def canUnlockAll(boxes):
    """
    takes in a list of lists (boxes)
    checks if all the boxes have the keys for them to be unlocked
    the elements in the lists inside the main list are the keys
    each secondary list is a box
    zero indexed so box[0] is box zero
    and box 0 is already unlocked.
    
    optimizations: if box 0 has no keys, the function automatically returns false

    param:
        boxes: a list of lists
    
    returns:
        boolean indicating whether all boxes are unlockable
    """