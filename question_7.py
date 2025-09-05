# Intersection of two arrays
List1 = [3, 4, 5, 1, 4, 6, 1, 7, 7] # Array 1
List2 = [5, 8, 2, 9, 9, 7, 7, 4, 6, 3] # Array 2
intersect = list(set(a) & set(b)) # Converting lists into set data type and using intersectio(&) and converting 
print(intersect)