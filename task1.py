import numpy as np

# Marks of students as array
marks = np.array([45, 78, 92, 60, 55])
print(f"Marks of students: {marks}")

# Adding grace marks to students who scored less than the specified limit
grace_limit = 60
grace_marks = 5
marks[marks < grace_limit] += grace_marks

# New array after adding grace marks
print(f"Marks of students after grace: {marks}")

# Average marks of class
mean_marks = np.mean(marks)
print(f"The new Average score is: {mean_marks}")
