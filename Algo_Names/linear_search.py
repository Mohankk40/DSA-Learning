
def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return True , i
  return False

names = ["Mohana", "Arjun", "Priya", "Ravi", "Anjali", "Karthik"]

print("%s, Index: %d" % linear_search(names, "Ravi"))