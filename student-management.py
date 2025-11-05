name = input("Enter your name: ")
class_name = input("Enter your class: ")
print("==================================================")
java = input("Enter your Java score (0-100): ")
java_score = float(java)
linux = input("Enter your Linux score (0-100): ")
linux_score = float(linux)
javascript = input("Enter your JavaScript score (0-100): ")
javascript_score = float(javascript)

print("==================================================")
print(f"Student Name: {name}")
print(f"Class Name: {class_name}")
average_score = (java_score + linux_score + javascript_score) / 3
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your average score is: {average_score:.2f}")
print(f"Your grade is: {grade}")