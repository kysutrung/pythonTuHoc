"""Bài tập: Đếm số lần xuất hiện của ký tự trong chuỗi
Yêu cầu: Viết một chương trình đếm số lần xuất hiện của
một ký tự trong một chuỗi."""

kytu = input('ky tu can dem: ')
chuoi = input('nhap chuoi can tim: ')
count = 0
for i in chuoi:
    if kytu == i:
        count += 1
print("so lan ky tu xuat hien la: ", count)