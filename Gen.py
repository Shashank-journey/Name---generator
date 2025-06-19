import random

names = ["shadow", "hunter", "cypher", "byte", "nova", "drift"]
numbers = str(random.randint(10, 999))
symbol = random.choice(["_", "-", "x", ""])

username = random.choice(names) + symbol + numbers
print("🔥 Your hacker tag is:", username)