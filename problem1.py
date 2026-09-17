def flatten(nested_list):
  """
  nested list -> flattened list
  flatten takes in a list with internal nesting and returns a single list

  >>> flatten([1,[[2],3],4,[5,6]])
  [1,2,3,4,5,6]
  
  >>> flatten([1,[4,5],6,[7,[9]]])
  [1,4,5,6,7,9]
  
  >>> flatten([[4,5],6,[9]])
  [4,5,6,9]
  """
  result = []
  for x in nested_list:
    if isinstance(x, list):
      result.extend(flatten(x))
    else:
      result.append(x)
  return result




  
