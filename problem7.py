from numpy import random

# Create a list of 3000 randomly generated integers between 0 and 10
rng=random.default_rng(seed=23)
random_nums=list(rng.integers(0,10, size=3000))
random_nums=[int(x) for x in random_nums]

path="random.txt" # The file "random.txt" will live in the current directory

### your code goes here
