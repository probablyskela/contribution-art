from datetime import datetime
from pathlib import Path

from git.repo import Repo


N = 100
repo = Repo(Path(__file__).parent.absolute())

for i in range(N):
    repo.index.commit(f"Commit: {datetime.now()} {i}")
