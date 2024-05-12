from pathlib import Path

path = Path("emails")
path.mkdir()
print(path.exists())
path.rmdir()

path = Path()
for file in path.glob("*"):
    print(file)