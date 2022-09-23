def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    print(numbers)
    biggest_number = 1
    for num in numbers:
        if num > biggest_number:
            biggest_number = num
        else:
            pass
    print(biggest_number)
    return biggest_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
