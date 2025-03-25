def quicksort(arr):
  if(len(arr) <= 1):
    return arr
  less_than_pivot = []
  greater_than_pivot = []
  pivot = arr[0]
  for i in arr[1:]:
    if i <= pivot:
      less_than_pivot.append(i)
    else:
      greater_than_pivot.append(i)
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

arr = [64, 25, 12, 22,22, 11] 

print(quicksort(arr))