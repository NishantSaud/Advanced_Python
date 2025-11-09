# Given a list of exam scores,
# filter out all below passing score (less than 50)
# then map remaining scores to letter grades

scores = [45, 55, 68, 72, 81, 90, 99, 38, 60, 77]

# Filter passing scores
passing_scores = list(filter(lambda s: s >= 50, scores))

# Convert to letter grades
grade_map = list(map(
    lambda s: 'A' if s >= 90 else
              'B' if s >= 80 else
              'C' if s >= 70 else
              'D' if s >= 60 else
              'E',
    passing_scores
))

print("Original scores:", scores)
print("Passing scores:", passing_scores)
print("Letter grades:", grade_map)
