from typing import List


def sum_list(lst: List[int]) -> int:
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: sum the first element with the sum of the rest of the list
    else:
        rest_sum = sum_list(lst[1:])
        print(f"Step for lst = {lst}, res = {lst[0] + rest_sum}")
        return lst[0] + rest_sum


# Test the function
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
