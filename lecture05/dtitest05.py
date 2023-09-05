#คำนวนเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน และคำนวณแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังค์ชัน ขอ 2 ฟังค์ชัน
#cast/conversation

#รับค่าข้อมูล
def inputใส่เงินของบุคคล():
    money = float(input('ป้อนเงิน : '))
    person = int(input('ป้อนคน: '))
    return money,person

#คำนวน และแสดงผล
def calAndShowMoneyShare(money,person):
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันขอเป็นเลขจำนวนเต็มปัดขึ้น

    doublefloatmoney = "%.2f" % money
    
    print(f'จำนวนเงิน {money:.2f} บาท {person} คน แชร์กันคนละ {round(money/person)} บาท')
    print('จำนวนเงิน' , doublefloatmoney, 'บาท' ,person, 'คน แชร์กันคนละ' ,(round(money/person)), 'บาท')
    print('จำนวนเงิน' +str("%.2f" % money) +'บาท' +str(person) +'คน แชร์กันคนละ' +str(round(money/person))+ 'บาท')
    print('จำนวนเงิน {:.2f} บาท {} คน แชร์กันคนละ {} บาท'.format(money), (person), (round(money/person)))
    print('จำนวนเงิน %s บาท %d คน แชร์กันคนละ %d บาท' %(doublefloatmoney,  person , round(money/person )))



money, person = inputใส่เงินของบุคคล()

calAndShowMoneyShare(money, person)

