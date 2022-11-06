import pickle
from typing import List


def save_hist_to_file(hist: List[int], filename: str):
    with open(filename, 'wb') as file:
        pickle.dump(hist, file)
        file.close()


def load_hist_from_file(filename: str) -> List[int]:
    with open(filename, 'rb') as file:
        hist = pickle.load(file)
        return hist        


def save_hists_to_file(histograms: List[List[int]], filename: str):
    with open(filename, 'wb') as file:
        pickle.dump(histograms, file)
        file.close


def load_hists_from_file(filename: str) -> List[List[int]]:
    with open(filename, 'rb') as file:
        hists = pickle.load(file)
        return hists       
