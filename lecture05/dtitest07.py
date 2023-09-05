#โปรแกรมคำนวนหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาตรทรงกลม 
#จากรัศมีที่ป้อนโดยผู้มใช้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ

#ขอ 5 ฟังก์ชัน
import math

#inputRadius
def inputRadius():
    # r = input('ป้อนR')
    #return r

    #หรือ r = float(input('ป้อนR:'))
    # return r

    # return input('ป้อนR:')

     return float(input('ป้อนR:'))

#calAreaCircle
def calAreaCircle(r):
    #area = math.pi * r ** 2
    #area = math.pi * r * 2
    #area = math.pi * math.pow(r,2)
    #return area
    return math.pi * math.pow(r,2)
    

#calRoundCircle 2 * pi * r
def calRoundCircle(r):
    #round = 2 * math.pi * r 
    return 2 * math.pi * r 


#calCubeCircle 4 / 3 * pi * r * r * r 
def calCubeCircle(r):
    #Cube = 4 / 3 * math.pi * r * r * r 
    return 4 / 3 * math.pi * r * r * r 


#showResult ขอทั้งหมดทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น ???? เส้นรอบวงเป็น ???? ปริมาตรทรงกลทเป็น ???? (^_-)db(-_^)
def showResult():
    radius = inputRadius()
    area = calAreaCircle(radius)
    perameter = calRoundCircle(radius)
    volume = calCubeCircle(radius)
    print('Radius:''%.4f' % radius)
    print('Area:''%.4f' % area)
    print('Perameter:''%.4f' % perameter)
    print('Volume:''%.4f' % volume)

showResult()

