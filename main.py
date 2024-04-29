from datetime import datetime
from pathlib import Path

from git.repo import Repo


N = 100
repo = Repo(Path(__file__).parent.absolute())
path = Path("text.txt")

with path.open("a") as file:
    repo.index.add(path)
    for i in range(N):
        file.write("*")
        repo.index.commit(f"Commit: {datetime.now()} {i}")
    file.truncate(0)
    repo.index.commit(f"Last Commit: {datetime.now()}")
