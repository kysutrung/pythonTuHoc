"""Bài tập 3: Tìm các phần tử chung giữa hai danh sách
Yêu cầu: Viết hàm tim_phan_tu_chung(list_a, list_b) để tìm các phần 
tử chung giữa hai danh sách list_a và list_b."""


list_a = ['u', 'hagwjfgy', 'Tuan', 56, 7]
list_b = ['Tuan', 85, 7, 'gfhgsh', 95]
chung1 = []
def Ptu_chung(list_c, list_d):
    for i in list_a:
        for y in list_b:
            if i == y:
                chung1.append(i)
Ptu_chung(list_a, list_b)
print(chung1)