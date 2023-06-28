#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    length = len(triangle) - 1
    for row in triangle:
        print(' ' * (length), end="")
        print("[{}]".format(",".join([str(x) for x in row])))
        length -= 1


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
