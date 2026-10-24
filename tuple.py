t = (10, 20, 30, 20, 40, 50, 20)

print("Tuple:", t)

print("Length:", len(t))

print("Count of 20:", t.count(20))

print("Index of 30:", t.index(30))

print("Maximum:", max(t))

print("Minimum:", min(t))

print("Sum:", sum(t))

print("Sorted:", sorted(t))

print("Reversed:", tuple(reversed(t)))

print("Membership:", 30 in t)

print("Membership:", 60 not in t)

print("Concatenation:", t + (60, 70))

print("Repetition:", (1, 2) * 3)

print("First Element:", t[0])

print("Last Element:", t[-1])

print("Slicing:", t[1:5])

print("Tuple Type:", type(t))

print("Tuple to List:", list(t))

print("List to Tuple:", tuple([1, 2, 3]))
