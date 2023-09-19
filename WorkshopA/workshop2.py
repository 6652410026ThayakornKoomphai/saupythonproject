def StudentDetails() :
    stuID = int(input("ใส่ ID นักเรียน: "))
    stuName = input("ใส่ชื่อนักเรียน: ")
    stuResult_1 = float(input("ใส่คะแนนผลครั้งที่ 1: "))
    stuResult_2 = float(input("ใส่คะแนนผลครั้งที่ 2: "))
    stuResult_3 = float(input("ใส่คะแนนผลครั้งที่ 3: "))
    return stuID, stuName, stuResult_1, stuResult_2, stuResult_3

stuID, stuName, stuResult_1, stuResult_2, stuResult_3 = StudentDetails()

def calAverageScore() :
    return  (stuResult_1 + stuResult_2 + stuResult_3) / 3

def showResult() :
    print(f"{stuID} {stuName} you have average score {calAverageScore():.2f}")

showResult()








