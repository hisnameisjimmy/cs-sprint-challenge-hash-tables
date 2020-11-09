def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Let's try this stupid, insane problem
    result = []
    dict = {}

    for array in arrays:
        for number in array:
            if not number in dict:
                dict[number] = 1
            else:
                dict[number] += 1
                if dict[number] == len(arrays):
                    result.append(number)
    print(result)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
