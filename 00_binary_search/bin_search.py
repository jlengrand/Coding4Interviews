"""
Binary search implementation
@jlengrand
2013/07

Binary search solves the problem [of searching within a pre-sorted array] by
keeping track of a range within the array in which T [i.e. the sought value]
must be if it is anywhere in the array.  Initially, the range is the entire
array.
The range is shrunk by comparing its middle element to T and discarding half the
range.  The process continues until T is discovered in the array, or until the
range in which it must lie is known to be empty.  In an N-element table,
the search uses roughly log(2) N comparisons.
"""

def bin_search(arr, t):
    """
    Performs binary search on the input array.
    Searches for t in arr, using a binary search.
    Returns True if t is found, False otherwise.
    """
    try:
        length = len(arr)
    except TypeError:
        return False

    if arr is None or length < 1 :
        return False

    if length == 1:
        return True if (arr[0] == t) else False





    return False


