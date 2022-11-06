from typing import List
from math import sqrt

def hist_distance(hist1: List[int], hist2: List[int]) -> float:
    distace = 0
    if len(hist1) != len(hist2):
        print('error, hist lenths are not equal')
        return

    element_id = 0
    while element_id < len(hist1):
        distace += (hist1[element_id] - hist2[element_id]) ** 2
        element_id += 1

    return sqrt(distace)
