def StudentNumber() :
    stuNumber = int(input("ใส่จำนวนของนักเรียน: "))
    return stuNumber

def gradeCheck(gradeAverage) :
    if gradeAverage > 2.00 :
        return "สอบผ่าน"
    else :
        return "สอบไม่ผ่าน"

def stuLoopAndShow() :
    for i in range(StudentNumber()):
        stuID = int(input("ใส่ ID นักเรียน: "))
        stuName = input("ใส่ชื่อนักเรียน: ")
        gradeAvg = float(input("ใส่เกรดนักเรียน: "))
      
        print("----------GRADE CHECKER---------")
        print(f"{stuID} {stuName} คุณได้เกรด {gradeAvg}  ดังนั้นคุณ{gradeCheck(gradeAvg)}")
        

stuLoopAndShow()
