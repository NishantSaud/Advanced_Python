# Given a dictionary of employee names and salaries,
# filter out employees earning less than $60,000
# then apply a 5% raise to the remaining salaries

employees = {
    "Alice": 55000,
    "Bob": 62000,
    "Charlie": 75000,
    "Diana": 48000,
    "Ethan": 90000
}

# Filter employees with salary >= 60000
filtered_employees = dict(filter(lambda item: item[1] >= 60000, employees.items()))

# Apply 5% raise
raised_salaries = dict(map(lambda item: (item[0], item[1] * 1.05), filtered_employees.items()))

print("Original salaries:", employees)
print("Filtered employees (>= $60,000):", filtered_employees)
print("After 5% raise:", raised_salaries)
