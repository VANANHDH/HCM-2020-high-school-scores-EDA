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

not_take_exam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in students:
    for i in range(5, 16):
        if s[i] == "-1":
            not_take_exam[i - 5] += 1

not_take_exam_percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 11):
    not_take_exam_percentage[i] = round(not_take_exam[i] * 100 / total_student, 2)

import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()

y_pos = numpy.arange(len(subjects))

plt.bar(y_pos, not_take_exam_percentage, align='center', alpha=0.5)
plt.xticks(y_pos, subjects)

axis.set_ylim(0,100)

plt.ylabel('Percentage')
plt.title('Số học sinh không đăng ký thi - theo môn học')

rects = axis.patches

for rect, label in zip(rects, not_take_exam):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
    )
plt.show()
