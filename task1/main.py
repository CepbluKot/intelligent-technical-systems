import random
import time
import typing


# config
max_int = 1000
histogram_borders = [num for num in range(100, 1000, 100)]  # 100, 200, ... , 900
num_of_iterations = 100  # num of generated lists
num_of_elements_to_generate = 1000000  # num of elements in 1 list


histograms: typing.List[typing.List[int]] = []
histogram_creation_times = []


def generate_random_data(
    num_of_iterations, num_of_elements_to_generate
) -> typing.List[typing.List[int]]:
    list_with_data_lists: typing.List[typing.List[int]] = []

    for selected_list in range(0, num_of_iterations):

        insindexe_list = []
        for element_index in range(0, num_of_elements_to_generate):
            insindexe_list.append(random.randint(0, max_int))

        list_with_data_lists.append(insindexe_list)

    return list_with_data_lists.copy()


def create_histogram(
    histogram_borders: typing.List[int], input_data: typing.List[int]
) -> typing.List[int]:
    start_time = time.time()

    output: typing.List[int] = [0 for num in range(0, 9)]
    histogram_border_index = 0
    input_data.sort()

    occurences = 0
    last_histogram_border_index = len(histogram_borders) - 1

    index = 0
    while index < len(input_data) - 1:
        if input_data[index] < histogram_borders[histogram_border_index]:
            occurences += 1
            index += 1

        elif (
            histogram_border_index == last_histogram_border_index
            and input_data[index] >= histogram_borders[histogram_border_index]
        ):
            output[histogram_border_index] = occurences

            occurences += 1
            index += 1
            output[histogram_border_index] = occurences
        else:
            output[histogram_border_index] = occurences
            histogram_border_index += 1
            occurences = 0

            while (
                input_data[index] >= histogram_borders[histogram_border_index]
                and not histogram_border_index == last_histogram_border_index
            ):
                histogram_border_index += 1

    output[histogram_border_index] = occurences

    end_time = time.time()


    # print('[test #', test_id,'] INPUT: ' , input_data)
    # print('\n[test #', test_id,'] OUTPUT: ' , output)

    # print('\n[test #', test_id,'] TIME: ' , end_time - start_time)
    # print('\n')

    return output.copy(), end_time - start_time


if __name__ == "__main__":
    results = []
    results_times = []
    random_data_lists = generate_random_data(
        num_of_iterations=num_of_iterations,
        num_of_elements_to_generate=num_of_elements_to_generate,
    )

    for selected_data in random_data_lists:
        result, result_time = create_histogram(
            histogram_borders=histogram_borders, input_data=selected_data
        )
        results_times.append(result_time)
        results.append(results)

    print(
        "\n TEST RESULT: min=",
        min(results_times),
        " max=",
        max(results_times),
        " avg=",
        sum(results_times) / len(results_times),
    )
