# OOP
# Camel case / Pascal case, Snake case
class DtiSau:
    # data/property member ค่าข้อมูล
    stu_name =''
    score = 0
    gpa = 0

    # method member คือการทำงาน
    def hiStudent(self):
        print(f'สวัสดี{self.stu_name}')

    def showScoreAndGrade(self):
        print(f'คะแนน{self.score} ได้gpa {self.gpa}')

# สร้าง Object
obj01 = DtiSau() # ชื่อคลาสที่มี () เราเรียกว่ามีการสั่งให้ constructor ของคลาสทำงาน
obj02 = DtiSau()

obj01.stu_name = "สมชาย"
obj01.hiStudent()
obj02.stu_name = "สมหญิง"
obj02.score = 90
obj02.gpa = "A"
obj02.hiStudent()
obj02.showScoreAndGrade()