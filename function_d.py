def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    if not numbers:
        return None
    
    max_num = None
    for num in numbers:
        if max_num is None or max_num < num:
            max_num = num
    
    return max_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
