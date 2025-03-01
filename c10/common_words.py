from pathlib import Path

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 
             'little_women.txt']

for file in filenames:
    path = Path(file)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"File {path} not found.")
    else:
        the_count = contents.count('the ')
        print(f"{path} has {the_count} the in it.")
