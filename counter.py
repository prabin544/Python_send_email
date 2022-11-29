"""
Write a script which will count number of files with each extension in a file tree. It should take the
initial directory as a command line argument, and then display the total number of files with each
distinct file extension that it finds. Files with no extension should be skipped. Use a Counter object to
do the counting.
"""

# import sys
# import os
# from collections import Counter

# start_dir = input("Enter Dir name: ")

# counter = Counter()

# for curr_dir, dir_list, file_list in os.walk(start_dir):
#     for file_name in file_list:
#         if '.' in file_name:
#             base, ext = os.path.splitext(file_name)
#             counter[ext] += 1

# for ext, count in counter.items():
#     print(ext, count)
# print()

# print(counter.most_common(10))

"""
Write a script which creates a named tuple President, with fields lastname, firstname, birthplace,
birthstate, and party. Read the data from Presidents.csv into an array of 44 President tuples.
Write the array out to a file named potus.pic. (use the Pickle module).
"""
# import pickle
# from pprint import pprint

# with open('../TEMP/pickled_data.pic', 'wb') as pic_out: 
#   pickle.dump(data, pic_out) 
# with open('../TEMP/pickled_data.pic', 'rb') as pic_in: 
#   pickled_data = pickle.load(pic_in) 
# pprint(pickled_data) 

"""
Read in the data from float_values.txt and print out the sum of all values. Do this with functional tools
– there should be no explicit loops in your code.
"""
from operator import add, mul
from functools import reduce

with open ('./DATA/float_values.txt') as fv:
    sum = reduce(add, map(float, fv))

print("{:.2f}".format(sum))

"""
Using presidents.txt, print out a list of the number of presidents from each state.
"""

with open ('./DATA/presidents.csv') as pf:
    print(lambda row : row.split(',')[6])