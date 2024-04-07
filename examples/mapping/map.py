def my_map(transform, array):
    if len(array) == 0:
        return []
    
    return [transform(array[0])] + my_map(transform, array[1:])

print(my_map(lambda x: x + x, [1, 2, 3, 4, 5]))