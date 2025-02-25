numbers = {
    'Jacob': [22, 2],
    'Emily': [10, 32],
    'Steve': [6, 25],
    'Becky': [14, 54],
    'Molly': [8, 14],
}

for name, nums in numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for num in nums:
        print(num)
    print()
