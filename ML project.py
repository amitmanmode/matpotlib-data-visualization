import matplotlib.pyplot as plt

# Dataset
students = ["Amit", "Ravi", "Riya", "Raj", "Priya"]

math_marks = [85, 78, 90, 72, 88]
science_marks = [80, 75, 92, 70, 85]
study_hours = [5,4,6,3,5]

# 1️⃣ Line Graph
plt.figure()
plt.plot(students, math_marks, marker='o')
plt.title("Math Marks Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2️⃣ Bar Graph
plt.figure()
plt.bar(students, science_marks)
plt.title("Science Marks Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3️⃣ Scatter Plot
plt.figure()
plt.scatter(study_hours, math_marks)
plt.title("Study Hours vs Math Marks")
plt.xlabel("Study Hours")
plt.ylabel("Math Marks")
plt.show()

# 4️⃣ Histogram
all_marks = math_marks + science_marks

plt.figure()
plt.hist(all_marks)
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5️⃣ Pie Chart
total_marks = [sum(math_marks), sum(science_marks)]

plt.figure()
plt.pie(total_marks, labels=["Math", "Science"], autopct="%1.1f%%")
plt.title("Subject Contribution")
plt.show()