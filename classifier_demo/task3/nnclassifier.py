import pickle
from typing import List
from task2 import hist_distance


class Hist:
    def __init__(self, data: List[int], class_id: int) -> None:
        self.data = data
        self.class_id = class_id

    def get_data(self):
        return self.data

    def get_class_id(self):
        return self.class_id


class HistForCompare(Hist):
    def set_distance(self, dist):
        self.dist = dist

    def get_distance(self):
        return self.dist


class NNClassifier:
    hists_storage: List[Hist] = []

    def __sort_for_compare(self, hist_for_compare: HistForCompare):
        try:
            return hist_for_compare.get_distance()
        except:
            print("error - sort")

    def load_hists_from_file(self, filename: str, class_id: int) -> List[List[int]]:
        try:
            with open(filename, "rb") as file:
                hists = pickle.load(file)

                for hist in hists:
                    new_hist_data = Hist(data=hist, class_id=class_id)
                    self.hists_storage.append(new_hist_data)
        except:
            print("error - load from file")

    def classify(self, hist: List[int]):
        try:
            distances: List[HistForCompare] = []
            for select_hist in self.hists_storage:
                dist = hist_distance.hist_distance(select_hist.get_data(), hist)
                hist_copy = HistForCompare(
                    data=select_hist.get_data(), class_id=select_hist.get_class_id()
                )
                hist_copy.set_distance(dist)

                distances.append(hist_copy)

            distances.sort(key=self.__sort_for_compare)
            for z in distances[2::-1]:
                print("HIST_DATA: ", z.data, "DIST: ", z.dist, "CLASS: ", z.class_id)

            return distances[2::-1]
        except:
            print("error - classifier")
