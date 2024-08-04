def selection_sort(elements):
    n = len(elements)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if elements[j] < elements[min_idx]:
                min_idx = j
        elements[i], elements[min_idx] = elements[min_idx], elements[i]
    return elements

elements = [22, 13, 4, 8, 17, 26, 53, 4]
print("Original elements:", elements)

sorted_elements = selection_sort(elements)
print("Sorted elements:", sorted_elements)