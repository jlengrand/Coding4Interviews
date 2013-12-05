"""
Implementation of the MergeSort algorithm

@jlengrand
2013/12
"""

class TableSorter():
    """
    A utili=ty that provides way to sort arrays of elements.
    It should be possible to compare elements to each others
    (meaning a > b and a == b should make sense).
    """

    #empty for now
    def __init__(self):
        pass

    def mergeSort(self, table, idx_min=1, idx_max=None):
        """
        Returns the table array sorted between
        indices idx_min and idx_max using the merge sort algorithm
        """
        if len(table) < 1:
            return None

        if idx_max == None:
            idx_max = len(table)

        #TODO: Implement
        return None
