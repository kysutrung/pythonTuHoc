"""Bài tập 4: Xoay vòng danh sách
Yêu cầu: Viết hàm xoay_vong_danh_sach(list_a, k) để xoay vòng 
danh sách list_a sang phải k vị trí."""

k = int(input("dich sang: "))
a = [10, 20, 30, 40, 50, 60]
a[:0] = a[len(a) - k:]
b = a[0:len(a)-k]
print(b)