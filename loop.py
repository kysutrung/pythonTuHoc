"""Bài Tập 1: Vòng Lặp for – Tìm Số Nguyên Tố
Mô Tả Bài Tập:
Viết một chương trình Python sử dụng vòng lặp for để kiểm tra xem một số nguyên n có phải là số nguyên tố hay không. Một số nguyên tố là số lớn hơn 1 chỉ chia hết cho 1 và chính nó.
"""
"""import math
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
    print("n khong la so nguyen to")"""


"""Bài Tập 2: Vòng Lặp while – Tính Dãy Fibonacci
Mô Tả Bài Tập:
Viết một chương trình Python sử dụng vòng lặp while để in ra n số đầu tiên trong dãy Fibonacci, trong đó n được nhập từ bàn phím."""


n = int(input("Nhập n số Fibonacci cần in: "))
def fibonacci(n):
    so1, so2 = 0, 1
    count = 0
    
    while count < n:
        print(so1, end=' ')
        so1, so2 = so2, so1 + so2
        count += 1
fibonacci(n)




