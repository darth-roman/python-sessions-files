########## Lists ##########
# Can store multiple values at once of diff data types
# Assigned to one variable name
# Some other programming languages call them arrays
# Some other programming languages do not accept the mixture of types in one array/list

# random_list = ["Louai", "Maria", False, "Marie", "Meriem", 15, 2.5]
# attended_students = ["Chaima", "Chams", "Batoul", "Loudjein", "Rofaida", "Sara", "Alaa"]
# print(attended_students)
students = ["Louai", "Maria", "Marie", "Meriem", "Aya", "Sara"]
# print(f"Original List: {students}")
# print(f"List access: {students[5]}")

# print(f"Last Item: {students[-4]}")

# You can use the elements based on the rules of the specific accessed element
# Example:
# print("FOX IN THE BOX")
# numbers = [1,2,3,4,5,6]
# print(numbers[0]+numbers[-1])
#print(f"Last Item: {students[0].upper()}")

# Modifying elements of the list
# students[6] = "Ahmed"
# print(students)

# Adding to the list
## Appending
# students.append("Soufiane")
# print(f"List After Appending '{students[-1]}': {students}")

## Inserting
# students.insert(-1, "Merouane")
# print(f"List After Intserting '{students[-1]}': {students}")

# Deleting from the list
## del
### Selective position
# del students[-1]
# print(students)

## pop()
### Deleting from the end / return the latest item


# students = ["Louai", "Maria", "Marie", "Meriem", "Aya", "Sara"]
# poppedStudent = students.pop() # Sara / "Louai", "Maria", "Marie", "Meriem", "Aya"
# poppedStudent = students.pop() # Aya /  "Louai", "Maria", "Marie", "Meriem"
# poppedStudent = students.pop()
# print(poppedStudent)
# print(students)


# Pop from a selective position
# student = students.pop(3)
# print(student)
# print(students)
# Remove by value
# students.remove("Aya")
# print(students)

# Sorting a List
## Permanently
# students.sort()
# print(students)

## Temporarily
# sortedList = sorted(students)
# print(sortedList)
# print(students)

# Bonus: Reverse the order of a List (Guess how it affectes it, perma or tempo?)
# students.reverse()
# print(students)

# size of a list
print(len(students))

########## Dictionaries ##########

# key-value pair
# they key part is similar to a variable
# the value can be anything: int, string, list ...

# Example
normal_values = {
    "glucose": {
        "normal_range": [70, 99],
        "unit":"mg/dL"
    },
    "testosterone": {
        "normal_male": [300, 1000],
        "normal_female": [17, 70],
        "unit":"ng/dL"
    },
    "cortisol": {
        "normal_morning": [10, 20],
        "normal_afternoon": [3, 10],
        "unit":"mcg/dL"
    }
}

test_result = {
    "glucose": "150",
    "testosterone": {
        "male": "512",
        "female": "35"
    },
    "cortisol": {
        "morning": "14.67",
        "afternoon": "5.23"
    }
}

# print(f"{test_result['glucose']} {normal_values['glucose']['unit']}")

# gluNormalVals = normal_values["glucose"]["normal_range"]
# glucoseUnit = normal_values["glucose"]["unit"]
# glucoseTest = float(test_result["glucose"])
# if glucoseTest in range(min(gluNormalVals), max(gluNormalVals)):
#     print(f"with a {glucoseTest}{glucoseUnit}, you will be fine")
# else:
#     print(f"with a {glucoseTest}{glucoseUnit}, how are you still alive")









