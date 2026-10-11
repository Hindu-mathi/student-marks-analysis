students = { 
"Priya": [80, 90, 85],
"Rahul": [70, 75, 80],
"Divya": [90, 95, 92]
}
for name, marks in
students.items():
  total = sum(marks)
  percentage = total / 3

print("student:", name)
print("total marks:", total)
print("percentage:", percentage)

if percentage >=35:
  print("result: pass")
else:
  print("result: fail")

print("-------------------")
