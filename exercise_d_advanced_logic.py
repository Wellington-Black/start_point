# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_integers = []
for number in numbers:
  if (number % 2 == 0):
    even_integers.append(number)
print(even_integers)

# 2. Print the difference between the largest and smallest value:
min_value = min(numbers)
max_value = max(numbers)
diff = max_value - min_value
print(diff)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
index = 0
while (index < len(numbers)):
    if (numbers[index] == 2 and numbers[index+1] == 2 ):
        print(True)
    # else:
    #     print(False)
    index += 1
    

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







