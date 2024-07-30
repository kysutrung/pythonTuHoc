"""Bài Tập 1: Vòng Lặp for – Tìm Số Nguyên Tố
Mô Tả Bài Tập:
Viết một chương trình Python sử dụng vòng lặp for để kiểm tra xem một số nguyên n có phải là số nguyên tố hay không. Một số nguyên tố là số lớn hơn 1 chỉ chia hết cho 1 và chính nó.
"""
import math
global n 
n = int(input("Nhap 1 so nguyen n: "))
def sont(n):
    if n < 1:
        print('Khong phai so nguyen to')
    for i in range (2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    else:
        return True 
if sont(n):
    print("n la so nguyen to")
else:
    print("n khong la so nguyen to")


  