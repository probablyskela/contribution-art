from pathlib import Path

N = 100

with Path("text.txt").open() as file:
    for _ in range(N):
        file.write("i")


    file.truncate(0)
