
def binary_search(names, target):
  first = 0
  last = len(names) - 1
  while  first <= last:
    mid = (first + last) // 2
    if names[mid] == target:
      return mid
    elif names[mid] < target:
      first = mid + 1
    else:
      last = mid - 1
  return None

names = ["Anjali", "Arjun", "Karthik", "Mohana", "Priya", "Ravi"]

print("Index: %d" % binary_search(names, "Arjun"))