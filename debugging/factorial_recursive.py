#!/usr/bin/python3
import sys

def factorial(n):
    """
        Function Description:
            Recursively calculates the factorial of a non-negative integer n.

        Parameters:
            n (int): A non-negative integer for which the factorial is computed.

        Returns:
            int: The factorial of n. If n is 0, returns 1 as 0! = 1.
        """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)