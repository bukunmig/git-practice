def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    print(numbers)
    biggest_number = 1
    for num in numbers:
        if num > biggest_number:
            biggest_number = num
        else:
            pass
    print(biggest_number)
    return biggest_number
=======
    largest_number = max(numbers)
    return largest_number
>>>>>>> b58773a87c5d5d0b877e118d1ab839fdd05d9396


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
