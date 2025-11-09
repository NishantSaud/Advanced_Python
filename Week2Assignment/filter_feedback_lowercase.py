# Given a list of customer feedback strings,
# filter out feedback messages shorter than 20 characters
# then convert the remaining messages to lowercase

feedback = [
    "Great service!",
    "The product quality was excellent and delivered on time.",
    "Okay.",
    "Amazing experience, will buy again!",
    "Fast shipping!"
]

# Filter feedback with 20 or more characters
long_feedback = list(filter(lambda msg: len(msg) >= 20, feedback))

# Convert to lowercase
lowercase_feedback = list(map(lambda msg: msg.lower(), long_feedback))

print("Original feedback:", feedback)
print("Filtered feedback (>= 20 chars):", long_feedback)
print("Lowercased feedback:", lowercase_feedback)
