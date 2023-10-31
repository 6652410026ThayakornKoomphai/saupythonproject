# คุณสมบัติ Encapsulation (ห่อหุ้ม data/attribute/field/property)
class DTItest05:
      #data
      infoA = 10 #ไม่ได้ห่อหุ้ม
      __infoB = 20 #Encap

      def __init__(self, infoC, infoD):
            self.infoC = infoC #ไม่ได้ Encap
            self.__infoD = infoD #Encap ดูจาก __??? -> เป็นการกำหนด access_modifier เป็น Private

      #เมื่อใดก็ตาม Encap จะต้องมีเมธอด 2 ตัวนี้เสมอ คือ get, set ของ data ตัวนั้น
      def setInfoB(self, infoB): # กำหนดค่าให้กับ data
          self.__infoB = infoB

      def getInfoB(self): # เอาค่า data ไปใช้
          return self.__infoB
      
      def setInfoD(self, infoD):
          self.__infoB = infoD

      def getInfoD(self):
          return self.__infoD
      
      def showInfo(self):
          print(self.infoA, end='')
          print(self.__infoB, end='')
          print(self.infoC, end='')
          print(self.__infoD)
          print('----------------------')

obj1 = DTItest05(30,40)
obj2 = DTItest05(30,100)
obj1.showInfo() # 10 20 30 40
obj1.infoA = 555
# obj1.__infoB = 999 # มันถูก Encap หรือ __ เอาไว้ค่าของมันเลยไม่เปลี่ยน
obj1.setInfoB(999)
obj1.showInfo() # 555 999 30 40
# print(obj1.__infoB + obj1.__infoD) มันถูก Encap ถ้าจะเอาค่าที่เก็บมาใช้งานต้องมาเมธอด get
print(obj1.getInfoB() + obj1.getInfoD())