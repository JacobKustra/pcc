from pathlib import Path

files = ['cats.txt', 'dogs.txt']

for file in files:
    path = Path(file)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"File {path} does not exist!")
    else:
        print(contents)
