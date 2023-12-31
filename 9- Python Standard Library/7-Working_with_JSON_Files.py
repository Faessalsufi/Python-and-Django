# javascript object notation

import json
from pathlib import Path
# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Gravity", "year": 2023}
# ]

# data = json.dumps(movies)


data = Path("movies.json").read_text()

movies = json.loads(data)
print(movies[0]["title"])
