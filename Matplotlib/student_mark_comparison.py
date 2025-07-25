import matplotlib.pyplot as plt

students = ['Alice', 'Bob', 'John', 'Charlie', 'David']

marks = [85, 72, 90, 65, 78]

plt.bar(students, marks, color='royalblue')

plt.title("Mark Comparison Chart")
plt.xlabel('Name of the students')
plt.ylabel('Marks')
plt.grid()

plt.show()