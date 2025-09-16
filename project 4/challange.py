import random

friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
#Method 1
print(random.choice(friends))

#Method 2
random_pick = random.randint(0,4)

print(friends[random_pick])
