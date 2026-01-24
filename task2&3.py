import pandas as pd

# Creating DataFrame
student_data = {
    "Name": ["ARZAAN", "Tejasv", "SAKSHI", "priya"],
    "Age": [19, 20, 20, 21],
    "Branch": ["electrical", "CSE", "Civil", "ECE"],
}
student_df = pd.DataFrame(student_data)
print("Student Data:", student_df)  # Original DataFrame

# Cleaning the data by converting to title case
student_df.Branch = student_df.Branch.str.title()
student_df.Name = student_df.Name.str.title()

# -----------TASK 2----------------
# Display names of students from Electrical branch
print(
    "\nStudents from Electrical Branch: ",
    student_df.loc[student_df.Branch == "Electrical", "Name"],
)

# Display names of CSE students older than 19
print(
    "\nCse students older than 19: ",
    student_df.loc[(student_df.Branch == "Cse") & (student_df.Age > 19), "Name"],
)

# -----------TASK 3----------------

# Sorting students by age and display their names and ages
print("\nSorted by age: \n", student_df.sort_values(by="Age")[["Name", "Age"]])
# Display statistical summary for age
print("\nStats for age: \n", student_df.describe())
