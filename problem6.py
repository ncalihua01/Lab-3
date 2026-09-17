def merge_sets(set1, set2):
  """
  set1 and set2 -> merged set
  """
  result = set()
  for x in set1:
    for y in set2:
      result.add(x + y)
  return result
  
def word_scramble_sets(letters):
  """
  world_scramble_sets returns a set containing all possible word scrambles

  >>> word_scramble_sets({"a", "b", "c", "c"})
  {"abc", "acb", "bac", "bca", "cab", "cba"}
  """
  if len(letters) == 1:
    return letters
  result = set()

  for letter in letters:
    remaining = letters - {letter}
    for word in word_scramble_sets(remaining):
      result.add(letter + word)
  return result
