"""
 * Author: Yago Iglesias
 * Source: python stdlib
 * Description: Different reads from stdin.
 * Usage: ./a.out < input.txt
"""
a = int(input())  # Read an int
raw = input()  # Read a string
s = "sep :) "; raw = raw.split(s)  # Split the string by the separator s (default is space)
ints = [int(x) for x in raw]  # Convert the splitted string to a list of ints
a, b, c = int(raw[0]), int(raw[1]), int(raw[2])  # Read 3 ints
