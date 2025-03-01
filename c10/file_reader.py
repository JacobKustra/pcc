from pathlib import Path

# path = Path('pi_digits.txt')
path = Path('pi_million_digits.txt')
contents = path.read_text()
# contents = path.read_text().rstrip()
# contents = contents.rstrip()
# for line in lines:
#     print(line)
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
