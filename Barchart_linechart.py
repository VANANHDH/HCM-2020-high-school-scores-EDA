with open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

header = header.split(",")
subjects = header[5:]

total_student = len(students)

for i in range(total_student):
    students[i] = students[i].split(",")

students.pop()

# get number of student per age group
# 2003 2002 2001 2000 ... 1994 <= 1993
#17 18 19 20 ... 26 >=27

num_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
average_of_student_per_age_group = [0,0,0,0,0,0,0,0,0,0,0]
for s in students:
	age = 2020 - int(s[4])
	if age >= 27:
		age = 27
	num_of_student_per_age_group[age - 17] += 1 #tuổi chạy từ 17 đến 27 nên trừ ra 17 sẽ ra index

	sum_score = 0 # Tổng điểm
	count_score = 0 # Số môn thi
	for i in range(11):
		if s[i+5] != "-1":
			count_score +=1
			sum_score += float(s[i+5])

	averrage = sum_score/count_score
	average_of_student_per_age_group[age - 17] += averrage

for i in range(len(average_of_student_per_age_group)):
	average_of_student_per_age_group[i] = average_of_student_per_age_group[i]/num_of_student_per_age_group[i]

# scale từ 0-10 lên 0-70000 -> nhân 7000 để vẽ kết hợp với barchart
for i in range(len(average_of_student_per_age_group)):
	average_of_student_per_age_group[i] = average_of_student_per_age_group[i] * 7000

# import library: matpotlib and numpy
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(11)
y = np.arange(11)

# create a bar chart
fig, axis = plt.subplots()
plt.bar(x, num_of_student_per_age_group)

# create a line chart
plt.plot(x, average_of_student_per_age_group, color='red', marker='o')

# set limit for y axis
axis.set_ylim(0,70000)

# label for column x
age_label = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, ">26"]
plt.xticks(x, age_label)

axis.set_ylabel('Số học sinh')
axis.set_xlabel('Tuổi')

# right side ticks
axis2 = axis.twinx()
axis2.tick_params('y', colors='r')
axis2.set_ylabel('Điểm trung bình')
axis2.set_ylim(0,10)

# set title
plt.title('Số học sinh dự thi và điểm trung bình theo độ tuổi')

# label for barchart
rects = axis.patches
labels = [2, 66327, 4463, 1396, 767, 384, 300, 223, 177, 109, 296]
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height + 1, label, ha="center", va="bottom"
    )
plt.show()


