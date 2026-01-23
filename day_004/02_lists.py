import random as rand

fruits = ["Apple", "Peach", "Pear"]

fruits[0] = "Grapes"

fruits.append("Strawberries")
fruits.extend(["Watermelon", "Tomatoes"])

print(fruits)

# [ 0,  1,  2,  3]
# [-4, -3, -2, -1]
# fruits.clear()
# print(fruits) 

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
for friend in friends:
    print(friend)
print("===")    
    
# 1st Option
print(rand.choice(friends))

# 2nd Option
random_index = rand.randint(0, len(friends) - 1)
print(friends[rand.randint(0, len(friends) - 1)])

fruits = ["Apple", "Peach", "Pear"]
vegetables = ["Spinach", "Kale", "Tomatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[0][1])
