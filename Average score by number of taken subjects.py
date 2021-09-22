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
average = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	count = 0
	total = 0
	for i in range(11):
		if s[i+5] != "-1":
			total += float(s[i+5])
			count +=1

	# if count == 11:
	# 	print(s)


	num_of_exam_taken[count] +=1
	average[count] += total/count #điểm trung bình bằng tổng điểm chia số môn

for i in range(12):
	if num_of_exam_taken[i] != 0:
		average[i] = round(average[i]/num_of_exam_taken[i], 2)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(12)
y = np.arange(12)

fig, axis = plt.subplots()
plt.bar(x, average, align='center', alpha=0.5)

axis.set_ylim(0,10)
plt.xticks(x, y)

plt.ylabel('Điểm trung bình')
plt.title('Điểm trung bình của nhóm thi các môn')

rects = axis.patches

labels = average
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height + 1, label, ha="center", va="bottom"
    )
plt.show()
