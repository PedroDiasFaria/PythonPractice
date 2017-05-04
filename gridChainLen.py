from numpy import ndenumerate


class GetIndices:
    """
    Maps value of a grid element to its corresponding index.
    e.g. indices[1] = (0, 1) for the first example grid
    """
    indices = []

    def __init__(self, Grid):
        # initialize empty list
        self.indices = [''] * len(Grid) ** 2

        for idx, val in ndenumerate(Grid):
            self.indices[val] = idx
            print(idx, val)


def is_neighbor(point1, point2):
    print("Point1:", point1, " and Point2:", point2,)
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    """
    Given two 2D points, return true if they are horizontally or vertically adjacent
    >>> is_neighbor((0, 0), (0, 1))
    True
    >>> is_neighbor((0,0), (1,0))
    True
    >>> is_neighbor((0,0), (1,1))
    False
    """
    if (x1 == x2 and (y1 in range(y2 - 1, y2 + 2))) or (y1 == y2 and (x1 in range(x2 - 1, x2 + 2))):
        print("are neighbors")
        return True
    else:
        print("are not neighbors")
        return False


def get_longest_chain(Grid):
    """
    Returns the length of the longest chain of consecutive numbers in a MxM grid of natural numbers from 0 to N. 
    """
    grid_info = GetIndices(Grid)
    current_chain = 1
    max_chain = 0
    for idx in range(0, len(Grid) ** 2 - 1):
        if is_neighbor(grid_info.indices[idx], grid_info.indices[idx + 1]):
            current_chain += 1
            if current_chain > max_chain:
                max_chain = current_chain
        else:
            current_chain = 1

    return max_chain


example_puzzle1 = [[0, 1, 4], [2, 3, 5], [8, 7, 6]]
example_puzzle2 = [[0, 2], [3, 1]]
print(get_longest_chain(example_puzzle1))
print(get_longest_chain(example_puzzle2))