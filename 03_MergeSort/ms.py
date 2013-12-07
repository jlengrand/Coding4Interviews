"""
Implementation of the MergeSort algorithm

@jlengrand
2013/12
"""

class TableSorter():
    """
    A utility that provides a way to sort arrays of elements.
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
        elif len(table) == 1:
            return table

        if idx_max == None:
            idx_max = len(table)

        t_1 = self.mergeSort(table[:len(table)/2])
        t_2 = self.mergeSort(table[len(table)/2:])

        return self._merge(t_1, t_2)

    def _merge(self, t_1, t_2):
        """
        Returns a sorted array t being the concatenation of values from t_1 and t_2.
        t_1 and t_2 are expected to be sorted themselves.
        """
        t = []

        while(t_1 != [] or t_2 != []):
            if(t_1 == []):
                t.append(t_2.pop(0))
            elif(t_2 == []):
                t.append(t_1.pop(0))
            else:
                if(t_1[0] < t_2[0]):
                    t.append(t_1.pop(0))
                else:
                    t.append(t_2.pop(0))

        return t

if __name__ == "__main__":
        table = [1, 2, 3, 4]
        sorter = TableSorter()
        sorter.mergeSort(table)