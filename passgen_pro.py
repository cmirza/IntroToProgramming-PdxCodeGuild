import random
import string

pass_length = int(input('How long of a password do you need?\n'))
prob = int(input('What percentage should be letters, not numbers?\n'))

for i in range(pass_length):
    if random.randint(0, 100) > prob:
        print(random.choice(string.digits), end="")
    else:
        print(random.choice(string.ascii_letters), end="")
print("\n")
