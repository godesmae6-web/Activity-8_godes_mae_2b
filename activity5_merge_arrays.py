# Activity 5: Merge k sorted arrays

import heapq


def merge_sorted_arrays(arrays):

    min_heap = []
    result = []

    
    for array_index in range(len(arrays)):

        if len(arrays[array_index]) > 0:
            first_value = arrays[array_index][0]

            heapq.heappush(
                min_heap,
                (first_value, array_index, 0)
            )

    
    while len(min_heap) > 0:

        value, array_index, position = heapq.heappop(min_heap)

        result.append(value)

       
        next_position = position + 1

        if next_position < len(arrays[array_index]):

            next_value = arrays[array_index][next_position]

            heapq.heappush(
                min_heap,
                (next_value, array_index, next_position)
            )

    return result



arrays = [
    [1, 5, 9],
    [2, 6],
    [0, 12]
]

print("ACTIVITY 5: MERGE K SORTED ARRAYS")
print("Input arrays:", arrays)

merged = merge_sorted_arrays(arrays)

print("Merged array:", merged)


print("Is fully sorted:", merged == sorted(
    value for array in arrays for value in array
))


print("\nADDITIONAL TESTS")

print("Different lengths:",
      merge_sorted_arrays([[1, 4], [2, 3, 8], [5]]))

print("Duplicates:",
      merge_sorted_arrays([[1, 2, 2], [2, 3], [1, 4]]))

print("Empty array:",
      merge_sorted_arrays([[1, 3], [], [2, 4]]))

print("All empty arrays:",
      merge_sorted_arrays([[], [], []]))