from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13, 22]

path = Path('number.json')
contents = json.dumps(numbers)
path.write_text(contents)
