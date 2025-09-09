"""
    สร้าง class Student โดยกำหนดให้
    - มี attribute ชื่อ name, age, และ student_id ที่เก็บข้อมูลทั่วไปของนักเรียน และ grades ที่เก็บคะแนนของนักเรียนในแต่ละวิชา โดยเป็นโครงสร้างข้อมูลประเภท list
    - มี method ชื่อ add_grade(subject, grade) โดย grade เป็น dictionary ที่เก็บคะแนนของนักเรียนในแต่ละวิชา
        { 
            "subject": "Mathematics", "grade": 85 
        }
    - มี method ชื่อ get_average_grade() ที่คืนค่าเฉลี่ยคะแนนของนักเรียน
    - มี method ชื่อ get_grade_report() ที่คืนค่ารายงานผลการเรียนของนักเรียน
"""

class Student:
    
    def __init__(self, name, age, student_id):
        self.name = name 
        self.age = age 
        self.student_id = student_id 
        self.grades = []

    # Method to add a grade
    def add_grade(self, grade):
        subject = grade.get("subject")
        score = grade.get("grade")

        if score < 0 or score > 100:
            return f"Error: Invalid score {score}. Must be between 0 and 100."

        for item in self.grades:
            if item["subject"] == subject:
                return f"Error: Subject '{subject}' already exists."

        self.grades.append(grade)
        return f"{grade} successfully added"    
        
    # Method to get the average grade
    def get_average_grade(self):
        if not self.grades:
            return 0
 
        total = 0 
        for grade in self.grades:
            total += grade["grade"]
        count = len(self.grades)
        average = total / count
        return average
    # Method to get the grade report
    def get_grade_report(self):
        report = f"Grade Report for {self.name} (ID: {self.student_id})\n"
        for grade in self.grades:
            report += f"- {grade['subject']}: {grade['grade']}\n"
        return report


student = Student("John", 20, "S123") 
#use print to return 
print(student.add_grade(
    {
        "subject": "Math", 
        "grade": 85
    }
))
student.add_grade(
    {
        "subject": "Science",
        "grade": 92
    }
)
print(student.get_average_grade())  # Should print 88.5
print(student.get_grade_report())   # Should show all grades