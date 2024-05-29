from datetime import datetime
from pathlib import Path

from git.repo import Repo


N = 200
repo = Repo(Path(__file__).parent.absolute())
path = Path("text.txt")

repo.index.add([path])
for i in range(N):
    with path.open("a") as file:
        file.write("*")
    repo.index.commit(f"Commit: {datetime.now()} {i}")

with path.open("a") as file:
    file.truncate(0)
    repo.index.commit(f"Last Commit: {datetime.now()}")
