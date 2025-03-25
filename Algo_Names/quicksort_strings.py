
def quicksort_strings(names):
  if len(names) <= 1:
    return names
  less_than_pivot = []
  more_than_pivot = []
  pivot = names[0]
  for name in names[1:]:
    if name <= pivot:
      less_than_pivot.append(name)
    else:
      more_than_pivot.append(name)

  return quicksort_strings(less_than_pivot) + [pivot] + quicksort_strings(more_than_pivot)

names = ["Mohana", "Arjun", "Priya", "Ravi", "Anjali", "Karthik"]

for n in quicksort_strings(names):
  print(n)