
#2. Given a list `[1,2,3,4]` print out all the values in the list multiplied by 20.

#for val in [1,2,3,4]:
#   print(val*20)

#3. Given a list `["Elie", "Tim", "Matt"]`, return a new list with only the first letter (`["E", "T", "M"]`).

#result = [person[0] for person in ["Elie", "Tim", "Matt"]]
#print(result)


#4. Given a list `[1,2,3,4,5,6]` return a new list of all the even values.

result = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
print(result)
