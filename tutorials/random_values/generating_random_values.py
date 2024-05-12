import random # imports the random package

members = ["jonh", "yug", "james", "jack"]

leader = random.choice(members)

print(f"The leader is {leader}!")

for i in range(3):
    print(random.randint(0,20))