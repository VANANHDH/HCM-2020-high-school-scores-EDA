with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

students.pop()
total_student = len(students)

header = header.split(",")
subjects = header[5:]

for i in range(total_student):
    students[i] = students[i].split(",")

num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	for i in range(11):
		if s[i+5] != "-1":
			count +=1

	# if count == 11:
	# 	print(s)


	num_of_exam_taken[count] +=1

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '0 môn', '1 môn', '2 môn','3 môn','4 môn','5 môn','6 môn','7 môn','8 môn','9 môn','10 môn','11 môn'
sizes = [0, 80, 122, 2598, 4334, 318, 2730, 64261, 0, 0, 0, 1]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
