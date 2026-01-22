import random as rand
import my_module as mm

print(mm.my_favourite_number)

random_integer = rand.randint(1, 100)
print(random_integer)

random_number = rand.random() * 10
print(random_number)

random_float = rand.uniform(1, 10)
print(random_float)

random_heads_or_tails = rand.randint(0, 1)
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")


