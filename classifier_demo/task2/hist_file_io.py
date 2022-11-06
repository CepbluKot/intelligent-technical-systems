import pickle
from typing import List


def save_hist_to_file(hist: List[int], filename: str):
    try:
        with open(filename, "wb") as file:
            pickle.dump(hist, file)
            file.close()
    except:
        print("error - save file")


def load_hist_from_file(filename: str) -> List[int]:
    try:
        with open(filename, "rb") as file:
            hist = pickle.load(file)
            return hist

    except:
        print("error - load file")


def save_hists_to_file(histograms: List[List[int]], filename: str):
    try:
        with open(filename, "wb") as file:
            pickle.dump(histograms, file)
            file.close
    except:
        print("error - save file")


def load_hists_from_file(filename: str) -> List[List[int]]:
    try:
        with open(filename, "rb") as file:
            hists = pickle.load(file)
            return hists
    except:
        print("error - load file")
