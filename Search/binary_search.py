def binary_search(list, target):
  first = 0
  last = len(list)-1

  while first <= last:
    midpoint = (first + last)//2
    if(target < list[midpoint]):
      last = midpoint - 1
    elif(target > list[midpoint]):
      first = midpoint + 1
    else:
      return midpoint
  return None

def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in the list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

verify(binary_search(numbers, 3))