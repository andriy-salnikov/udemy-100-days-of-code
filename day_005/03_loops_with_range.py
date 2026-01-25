# Range() function with For Loop
# range(start, stop, loop)

for number in range(1, 11):
    print(number)
    
for number in range(1, 11, 3):
    print(number)
    
# Exercise: Calculate the sum of all the even numbers from 1 to 100.
sum = 0
for number in range(1, 101):
    sum += number
print(sum)
