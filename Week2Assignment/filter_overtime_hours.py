# Given employee work hours in a week,
# filter out employees who worked less than 40 hours
# and convert the remaining hours to overtime hours (hours - 40)

hours = [35, 40, 45, 38, 50, 60, 39]

# Filter employees who worked 40 hours or more
eligible_hours = list(filter(lambda h: h >= 40, hours))

# Calculate overtime
overtime_hours = list(map(lambda h: h - 40, eligible_hours))

print("Original hours:", hours)
print("Eligible hours (>= 40):", eligible_hours)
print("Overtime hours:", overtime_hours)
