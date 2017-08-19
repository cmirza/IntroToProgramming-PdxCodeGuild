#Takes a string, splits it by commas, then randomly displays one of the split strings

import random

input_adj = input("Give me three adjectives seperated by commas:\n")
input_adj.split(", ")
splitAdjective = input_adj.split(", ")

print(random.choice(splitAdjective))
