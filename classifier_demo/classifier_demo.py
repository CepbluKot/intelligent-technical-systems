import sys

sys.path.append('../')

from task1 import main
from task2 import hist_file_io
from task3 import nnclassifier




histogram_borders = [num for num in range(100, 1000, 100)]


for class_id in range(10):
    results = []

    random_data_lists = main.generate_random_data(
        num_of_iterations=100,
        num_of_elements_to_generate=1000,
    )

    for selected_data in random_data_lists:
        result, result_time = main.create_histogram(
            histogram_borders=histogram_borders, input_data=selected_data
        )
        results.append(result)

    hist_file_io.save_hists_to_file(histograms=results, filename='class'+str(class_id))


classifier = nnclassifier.NNClassifier()

for class_id in range(10):
    classifier.load_hists_from_file(filename='class'+str(class_id), class_id=class_id)

# test data

test_data = main.generate_random_data(
        num_of_iterations=1,
        num_of_elements_to_generate=1000,
    )

test_hist, result_time = main.create_histogram(
                histogram_borders=histogram_borders, input_data=test_data[0]
            )

print('INPUT: ', test_hist)
print('\nTOP 3 NEAREST:')
classifier.classify(test_hist)
