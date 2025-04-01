def myFunction():
    """
    Get Code information from the file

    @param1: File object passed in after opening
    @return List containing dictionaries of all functions and classes in file
    """
    print("hi")

    x = 5
    x += 5

    return x

def myFunction2():
    """
    I'm about Zayd
    """
    print("hi")

    x = 5
    x += 5

    return x

def SearchLoop(list, val):
    """
    Search for the value and return the index
    """
   
    for i, v in enumerate(list):
        if v == val:
            return i

def mystery_1(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
    return arr

def mystery_2(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return mystery_2(n - 1) + mystery_2(n - 2)