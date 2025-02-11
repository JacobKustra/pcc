dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# wont work because tuples are immutable
# dimensions[0] = 350
print("Original dimenseions:")
for dimension in dimensions:
    print(dimension)

dimensions = (450, 150)
print("Modified dimenseions:")
for dimension in dimensions:
    print(dimension)
