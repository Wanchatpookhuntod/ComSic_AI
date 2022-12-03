#!/usr/bin/python3
import numpy as np

id = 123006 # ใส่รหัส นศ
sum_id = 0

for i in str(id):
    sum_id+=int(id)

print(f"{sum_id % 10} คือค่าที่ต้องเปลี่ยนเป็น 0 ของ array ที่กำหนดให้")
print(f"* ถ้าไม่มี {sum_id % 10} ให้ + 1 คือค่าที่ต้องเปลี่ยนเป็น 0 ของ array ที่กำหนดให้")
print(f"* ถ้าไม่มีอีก {sum_id % 10} ให้ - 1 คือค่าที่ต้องเปลี่ยนเป็น 0 ของ array ที่กำหนดให้")

np.random.seed(int(str(id)[3:]))
array = np.random.randint(1, 10, (10,10)) # array ที่กำหนดให้

print("\narray ที่กำหนดให้")
print(array)

# พื้นที่ ที่ใช้โค้ด ======================
