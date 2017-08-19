import random

input_adj = input("Give me three adjectives seperated by commas:\n")
input_adj.split(", ")
splitAdjective = input_adj.split(", ")

print(random.choice(splitAdjective))
