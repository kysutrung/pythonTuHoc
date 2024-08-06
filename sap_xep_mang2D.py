"""Bài tập 1: Sắp xếp danh sách con bên trong danh sách 2D
Yêu cầu: Viết hàm sap_xep_danh_sach_2d(list_2d) để sắp xếp mỗi danh sách
con bên trong danh sách 2D theo thứ tự tăng dần."""

list_b = [3, 6, 2, 10, 36, 90, 4, 22]
list_a = [[3, 6, 2, 1], [10, 3, 5, 18], [36, 90, 4, 22]]

def bubble_sort(list_n):
    m = 0
    while m < len(list_n):
        for o in range(0, len(list_n) -1):
            if list_n[o] > list_n[o+1]:
                list_n[o], list_n[o+1] = list_n[o+1], list_n[o]
        m += 1

for item in list_a:
    bubble_sort(item)
print(list_a)