a = [10, 20, 30, 40, 20]
print("Original List:", a)

a.append(50)
print("Append:", a)

a.extend([60, 70])
print("Extend:", a)

a.insert(1, 15)
print("Insert:", a)

a.remove(20)
print("Remove:", a)

a.pop()
print("Pop:", a)

print("Index:", a.index(30))

print("Count:", a.count(20))

a.sort()
print("Sort:", a)

a.reverse()
print("Reverse:", a)

b = a.copy()
print("Copy:", b)

b.clear()
print("Clear:", b)

print("Length:", len(a))

print("Maximum:", max(a))

print("Minimum:", min(a))

print("Sum:", sum(a))
