

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(len(student_heights)) # 5
print(sum(student_heights)) # suma del array
# average = sum(student_heights) / len(student_heights)

total_height = 0
for height in student_heights:
  total_height = total_height + height

total_length = 0
for numb in student_heights:
  total_length = total_length + 1

average = round(total_height / total_length)
print(average)

