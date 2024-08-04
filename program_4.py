def sequential_search(elements, target):
    for i, element in enumerate(elements):
        if element == target:
            return f"Element {target} found at index {i}"
    return f"Element {target} not found in the list"

elements = [1, 3, 5, 8, 10, 23, 35]
target = 10

result = sequential_search(elements, target)
print(result)