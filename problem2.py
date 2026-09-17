def merge(sorted_list1, sorted_list2):
  """
  sorted list 1 and sorted list 2 -> combined sorted list 1 and 2

  merge takes two sorted lists and returns a new list that 
  contains all of the elements in the two lists in sorted order
  >>> merge([3,4,5,6], [1,4,7,8])
  [1,3,4,4,5,6,7,8]
  
  >>> merge([11,13,15,17], [12,16,18])
  [11,12,13,15,16,17,18]
  
  >>> merge([0,3,5], [1,7,10])
  [0,1,3,5,7,10]
  """
  return sorted(sorted_list1 + sorted_list2)


  
