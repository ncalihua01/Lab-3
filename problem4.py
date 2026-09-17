letters = "catdog"
def scramble(letters):
  """
  string -> all possible strings formed by the characaters in "catdog"
  scramble takes the string "catdog" and returns all the possible strings 
  formed using the characters in the string
  >>> scramble(letters)
  ['catdog', 'catdgo', 'catodg', 'catogd', 'catgdo', 'catgod', 
  'cadtog', 'cadtgo', 'cadotg', 'cadogt', 'cadgto', 'cadgot', 
  'caotdg', 'caotgd', 'caodtg', 'caodgt', 'caogtd', 'caogdt', ...]
  
  """
  if len(letters) == 0:
    return [""]
  result = []
  for i in range(len(letters)):
    first = letters[i]
    remaining = letters[:i] + letters[i+1:]
    for word in scramble(remaining):
      result.append(first + word)
  return result
    

def word_scramble(letters):
    """
  input -> all possible strings formed by the characaters in that input (lists, strings, or tuples)
  word_scramble takes the input and returns all the possible strings 
  formed using the characters in that input which can be lists, strings, or tuples
  >>> word_scramble("pink")
  ['pink', 'pikn', 'pnik', 'pnki', 'pkin', 'pkni', 'ipnk', 'ipkn', 'inpk', 
  'inkp', 'ikpn', 'iknp', 'npik', 'npki', 'nipk', 'nikp', 'nkpi', 'nkip', 
  'kpin', 'kpni', 'kipn', 'kinp', 'knpi', 'knip']
  
  """
  if len(letters) == 0:
    return [""]
  result = []
  for i in range(len(letters)):
    first = letters[i]
    remaining = letters[:i] + letters[i+1:]
    for word in word_scramble(remaining):
      result.append(first + word)
  return result
