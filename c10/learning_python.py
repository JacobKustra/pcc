from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print('\nPrint all contents')
print(contents)

print('\nPrint line by line')
for line in contents.splitlines():
    print(line)
