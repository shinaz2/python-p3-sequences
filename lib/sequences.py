def print_fibonacci(length):
    """
    Prints the Fibonacci sequence up to the specified length.
    
    Args:
        length (int): The number of Fibonacci numbers to generate and print
    """
    fibonacci_list = [0, 1]
    
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        while len(fibonacci_list) < length:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        print(fibonacci_list)