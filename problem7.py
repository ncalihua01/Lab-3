from numpy import random
"""
# Take a list of 3000 randomly generated integers between 0 and 10. Write this data to a file called "random.txt" formatted so that the file has commas separating values,
# 3 values are printed per line, and the first line of the file reads "col1, col2, col3".

col1,col2,col3
0,6,4
6,2,1
6,1,1
6,6,8
4,2,2
...

"""

rng=random.default_rng(seed=23)
random_nums=list(rng.integers(0,10, size=3000))
random_nums=[int(x) for x in random_nums]

path="random.txt" # The file "random.txt" will live in the current directory

f=open(path, "w")
try:
  f.writelines("col1,col2,col3\n")
  for i in range(0, len(random_nums), 3):
    f.writelines(
      str(random_nums[i]) + "," +
      str(random_nums[i+1]) + "," +
      str(random_nums[i+2]) + "\n"
    )
    
except:
  print("Try again!")
else:
  print("You did it!")
finally:
  f.close()
